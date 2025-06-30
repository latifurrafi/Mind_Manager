from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer
from django.shortcuts import render


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

def index(request):
    total_tasks = Task.objects.count()
    return render(request, 'index.html',{
        'total_tasks': total_tasks
    })