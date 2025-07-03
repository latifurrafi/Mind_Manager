from .models import Task

def get_user_tasks_context(user):
    tasks = Task.objects.filter(user=user).values("title", "description", "priority", "status", "due_date")
    context = "\n".join([
        f"Title: {task['title']}, Status: {task['status']}, Due: {task['due_date']}, Priority: {task['priority']}"
        for task in tasks
    ])
    return f"User's current tasks:\n{context}"
