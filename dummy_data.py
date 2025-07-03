import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myapi.settings")

django.setup()
import random
from django.utils import timezone
from users.models import User, Task

# Create 10 dummy users
users = []
for i in range(21, 30):
    user = User.objects.create(
        username=f"user{i+1}",
        email=f"user{i+1}@example.com",
        full_name=f"User {i+1}",
    )
    users.append(user)

# Create 50 dummy tasks
PRIORITY_CHOICES = ['low', 'medium', 'high']
STATUS_CHOICES = ['pending', 'in-progress', 'completed']
CATEGORY_CHOICES = ['work', 'personal', 'others']

for i in range(50):
    Task.objects.create(
        user=random.choice(users),
        title=f"Task {i+1}",
        description=f"This is a description for task {i+1}",
        priority=random.choice(PRIORITY_CHOICES),
        status=random.choice(STATUS_CHOICES),
        category=random.choice(CATEGORY_CHOICES),
        due_date=timezone.now() + timezone.timedelta(days=random.randint(1, 30)),
        time_tracking=random.choice([True, False]),
    )

print("✅ 10 users and 50 tasks created successfully!")
