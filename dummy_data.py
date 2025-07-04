import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myapi.settings")

django.setup()

# Django shell commands to create dummy data
# Run these in Django shell: python manage.py shell

from django.contrib.auth.hashers import make_password
from django.utils import timezone
from datetime import datetime, timedelta
from users.models import User, Task  # Replace 'myapp' with your actual app name

# Create dummy users
users_data = [
    {
        'username': 'john_doe',
        'password': make_password('password123'),
        'email': 'john.doe@example.com',
        'full_name': 'John Doe',
        'is_active': True,
    },
    {
        'username': 'jane_smith',
        'password': make_password('password123'),
        'email': 'jane.smith@example.com',
        'full_name': 'Jane Smith',
        'is_active': True,
    },
    {
        'username': 'mike_wilson',
        'password': make_password('password123'),
        'email': 'mike.wilson@example.com',
        'full_name': 'Mike Wilson',
        'is_active': True,
    },
    {
        'username': 'sarah_brown',
        'password': make_password('password123'),
        'email': 'sarah.brown@example.com',
        'full_name': 'Sarah Brown',
        'is_active': True,
    },
    {
        'username': 'alex_johnson',
        'password': make_password('password123'),
        'email': 'alex.johnson@example.com',
        'full_name': 'Alex Johnson',
        'is_active': False,
    },
]

# Create users
users = []
for user_data in users_data:
    user = User.objects.create(**user_data)
    users.append(user)
    print(f"Created user: {user.username}")

# Create dummy tasks
tasks_data = [
    {
        'user': users[0],  # john_doe
        'title': 'Complete quarterly report',
        'description': 'Analyze sales data and prepare comprehensive quarterly business report for stakeholders.',
        'priority': 'high',
        'status': 'in-progress',
        'category': 'work',
        'due_date': timezone.now() + timedelta(days=7),
        'time_tracking': True,
    },
    {
        'user': users[0],  # john_doe
        'title': 'Team meeting preparation',
        'description': 'Prepare agenda and presentation materials for weekly team meeting.',
        'priority': 'medium',
        'status': 'pending',
        'category': 'work',
        'due_date': timezone.now() + timedelta(days=2),
        'time_tracking': False,
    },
    {
        'user': users[0],  # john_doe
        'title': 'Grocery shopping',
        'description': 'Buy groceries for the week including fruits, vegetables, and household items.',
        'priority': 'low',
        'status': 'pending',
        'category': 'personal',
        'due_date': timezone.now() + timedelta(days=1),
        'time_tracking': False,
    },
    {
        'user': users[1],  # jane_smith
        'title': 'Website redesign project',
        'description': 'Lead the complete redesign of company website with new branding and improved UX.',
        'priority': 'high',
        'status': 'in-progress',
        'category': 'work',
        'due_date': timezone.now() + timedelta(days=30),
        'time_tracking': True,
    },
    {
        'user': users[1],  # jane_smith
        'title': 'Dental appointment',
        'description': 'Regular dental checkup and cleaning appointment.',
        'priority': 'medium',
        'status': 'completed',
        'category': 'personal',
        'due_date': timezone.now() - timedelta(days=2),
        'time_tracking': False,
    },
    {
        'user': users[1],  # jane_smith
        'title': 'Book club meeting',
        'description': 'Monthly book club meeting to discuss "The Great Gatsby".',
        'priority': 'low',
        'status': 'pending',
        'category': 'others',
        'due_date': timezone.now() + timedelta(days=10),
        'time_tracking': False,
    },
    {
        'user': users[2],  # mike_wilson
        'title': 'Client presentation',
        'description': 'Present new marketing strategy to key client for approval.',
        'priority': 'high',
        'status': 'pending',
        'category': 'work',
        'due_date': timezone.now() + timedelta(days=5),
        'time_tracking': True,
    },
    {
        'user': users[2],  # mike_wilson
        'title': 'Fix kitchen sink',
        'description': 'Repair leaky kitchen sink faucet and replace worn gaskets.',
        'priority': 'medium',
        'status': 'in-progress',
        'category': 'personal',
        'due_date': timezone.now() + timedelta(days=3),
        'time_tracking': False,
    },
    {
        'user': users[2],  # mike_wilson
        'title': 'Volunteer at food bank',
        'description': 'Help serve meals at local food bank on Saturday morning.',
        'priority': 'low',
        'status': 'completed',
        'category': 'others',
        'due_date': timezone.now() - timedelta(days=1),
        'time_tracking': False,
    },
    {
        'user': users[3],  # sarah_brown
        'title': 'Code review',
        'description': 'Review pull requests from junior developers and provide feedback.',
        'priority': 'medium',
        'status': 'pending',
        'category': 'work',
        'due_date': timezone.now() + timedelta(days=1),
        'time_tracking': True,
    },
    {
        'user': users[3],  # sarah_brown
        'title': 'Gym workout',
        'description': 'Complete full body workout routine at the gym.',
        'priority': 'low',
        'status': 'completed',
        'category': 'personal',
        'due_date': timezone.now() - timedelta(hours=2),
        'time_tracking': False,
    },
    {
        'user': users[3],  # sarah_brown
        'title': 'Plan birthday party',
        'description': 'Organize surprise birthday party for best friend including venue, decorations, and guest list.',
        'priority': 'high',
        'status': 'in-progress',
        'category': 'others',
        'due_date': timezone.now() + timedelta(days=14),
        'time_tracking': False,
    },
    {
        'user': users[4],  # alex_johnson (inactive user)
        'title': 'Database backup',
        'description': 'Perform weekly database backup and verify integrity.',
        'priority': 'medium',
        'status': 'pending',
        'category': 'work',
        'due_date': timezone.now() + timedelta(days=7),
        'time_tracking': True,
    },
    {
        'user': users[0],  # john_doe
        'title': 'Learn Python Django',
        'description': 'Complete online Django tutorial and build a sample project.',
        'priority': 'medium',
        'status': 'in-progress',
        'category': 'personal',
        'due_date': timezone.now() + timedelta(days=21),
        'time_tracking': True,
    },
    {
        'user': users[1],  # jane_smith
        'title': 'Update resume',
        'description': 'Update resume with recent projects and achievements.',
        'priority': 'low',
        'status': 'pending',
        'category': 'personal',
        'due_date': timezone.now() + timedelta(days=15),
        'time_tracking': False,
    },
]

# Create tasks
tasks = []
for task_data in tasks_data:
    task = Task.objects.create(**task_data)
    tasks.append(task)
    print(f"Created task: {task.title} for {task.user.username}")

print(f"\nSummary:")
print(f"Created {len(users)} users")
print(f"Created {len(tasks)} tasks")

# Optional: Print some statistics
print(f"\nTask Statistics:")
print(f"High priority tasks: {Task.objects.filter(priority='high').count()}")
print(f"Medium priority tasks: {Task.objects.filter(priority='medium').count()}")
print(f"Low priority tasks: {Task.objects.filter(priority='low').count()}")
print(f"Pending tasks: {Task.objects.filter(status='pending').count()}")
print(f"In-progress tasks: {Task.objects.filter(status='in-progress').count()}")
print(f"Completed tasks: {Task.objects.filter(status='completed').count()}")
print(f"Work category tasks: {Task.objects.filter(category='work').count()}")
print(f"Personal category tasks: {Task.objects.filter(category='personal').count()}")
print(f"Others category tasks: {Task.objects.filter(category='others').count()}")