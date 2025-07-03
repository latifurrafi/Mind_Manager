import os
import joblib
from dotenv import load_dotenv
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from rest_framework import status, viewsets
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

import google.generativeai as genai

from .models import Task
from .serializers import TaskSerializer


# Load environment variables
load_dotenv()
api_key = os.environ.get("GOOGLE_API_KEY")
print('✅API Key LOADED..')
if not api_key:
    raise ValueError("GOOGLE_API_KEY not found in environment variables.")

# Configure Gemini
genai.configure(api_key=api_key)
chat_model = genai.GenerativeModel("gemini-2.0-flash")

# Load ML model
model = joblib.load('priority_model.joblib')


# ----------------------------- User Auth -----------------------------------
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        print("POST DATA:", request.POST)
        if form.is_valid():
            print("Form is valid!")
            user = form.save()
            print("User saved:", user)
            login(request, user)
            return redirect('index')
        else:
            print("Form errors:", form.errors)
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})




# ----------------------------- Task Views ----------------------------------

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


@login_required
def index(request):
    total_tasks = Task.objects.filter(user=request.user).count()
    return render(request, 'index.html', {
        'total_tasks': total_tasks
    })


class PredictPriorityView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        title = request.data.get("title", "")
        description = request.data.get("description", "")
        text = f"{title} {description}"
        predicted_priority = model.predict([text])[0]
        return Response({"predicted_priority": predicted_priority}, status=status.HTTP_200_OK)


# ----------------------------- Gemini Chatbot ------------------------------

def get_user_tasks_context(user):
    tasks = Task.objects.filter(user=user).values("title", "description", "priority", "status", "due_date")
    if not tasks:
        return "The user has no tasks currently."
    
    context = "\n".join([
        f"- Title: {task['title']}, Status: {task['status']}, Due: {task['due_date'].strftime('%Y-%m-%d %H:%M')}, Priority: {task['priority']}"
        for task in tasks
    ])
    return f"User's current tasks:\n{context}"


class GeminiChatBotView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user_message = request.data.get("message", "").strip()
        user = request.user

        if not user_message:
            return Response({"reply": "Please enter a message."}, status=status.HTTP_400_BAD_REQUEST)

        SYSTEM_INSTRUCTION = """
            You are a task assistant for a specific task management web application.
            Only answer questions related to the user's tasks, such as:
            - how to create/edit/delete tasks
            - show or update tasks
            - explain task fields
            - describe specific user tasks

            DO NOT answer questions outside of this domain. If the user asks anything unrelated to task management, politely respond with: 
            'Sorry, I can only help with task-related queries in your todo app.'
            """

        # Personalized task context
        tasks_context = get_user_tasks_context(user)

        # Final prompt
        final_prompt = f"{SYSTEM_INSTRUCTION}\n\n{tasks_context}\n\nUser asked: {user_message}"

        try:
            response = chat_model.generate_content(final_prompt)

            # Optional post-check for unrelated answers
            if "task" not in response.text.lower():
                return Response({"reply": "Sorry, I can only help with task-related queries in your todo app."})

            return Response({"reply": response.text.strip()}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=500)
