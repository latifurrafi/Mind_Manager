from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer
from django.shortcuts import render
import joblib
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

model = joblib.load('priority_model.joblib')

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

def index(request):
    total_tasks = Task.objects.count()
    return render(request, 'index.html',{
        'total_tasks': total_tasks
    })


class PredictPriorityView(APIView):
    def post(self, request):
        title = request.data.get("title", "")
        description = request.data.get("description", "")
        text = f"{title} {description}"
        predicted_priority = model.predict([text])[0]
        return Response({"predicted_priority": predicted_priority}, status=status.HTTP_200_OK)
