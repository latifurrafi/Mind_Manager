import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myapi.settings")

django.setup()

from django.utils import timezone
from datetime import datetime, timedelta
from users.models import Task  # Replace 'your_app' with your actual app name

# Create 20 dummy Task objects
dummy_tasks = [
    Task(
        title="Complete quarterly report",
        description="Prepare and submit the Q4 financial report including revenue analysis and projections",
        priority="high",
        status="in-progress",
        category="work",
        due_date=timezone.now() + timedelta(days=5),
        time_tracking=True
    ),
    Task(
        title="Buy groceries for the week",
        description="Purchase vegetables, fruits, dairy products, and household essentials",
        priority="medium",
        status="pending",
        category="personal",
        due_date=timezone.now() + timedelta(days=2),
        time_tracking=False
    ),
    Task(
        title="Schedule dentist appointment",
        description="Book routine dental checkup and cleaning appointment",
        priority="low",
        status="pending",
        category="personal",
        due_date=timezone.now() + timedelta(days=14),
        time_tracking=False
    ),
    Task(
        title="Update website content",
        description="Revise product descriptions and update company news section",
        priority="medium",
        status="completed",
        category="work",
        due_date=timezone.now() - timedelta(days=2),
        time_tracking=True
    ),
    Task(
        title="Plan birthday party",
        description="Organize venue, catering, and guest list for Sarah's birthday celebration",
        priority="high",
        status="in-progress",
        category="personal",
        due_date=timezone.now() + timedelta(days=8),
        time_tracking=False
    ),
    Task(
        title="Code review for new feature",
        description="Review pull requests for the user authentication module",
        priority="high",
        status="pending",
        category="work",
        due_date=timezone.now() + timedelta(days=1),
        time_tracking=True
    ),
    Task(
        title="Learn Spanish vocabulary",
        description="Study 50 new Spanish words and practice pronunciation",
        priority="low",
        status="in-progress",
        category="personal",
        due_date=timezone.now() + timedelta(days=7),
        time_tracking=True
    ),
    Task(
        title="Organize charity fundraiser",
        description="Coordinate local community fundraising event for animal shelter",
        priority="medium",
        status="pending",
        category="others",
        due_date=timezone.now() + timedelta(days=21),
        time_tracking=False
    ),
    Task(
        title="Fix laptop screen",
        description="Take laptop to repair shop to fix cracked display",
        priority="high",
        status="completed",
        category="personal",
        due_date=timezone.now() - timedelta(days=1),
        time_tracking=False
    ),
    Task(
        title="Prepare presentation slides",
        description="Create PowerPoint presentation for Monday's client meeting",
        priority="high",
        status="in-progress",
        category="work",
        due_date=timezone.now() + timedelta(days=3),
        time_tracking=True
    ),
    Task(
        title="Clean garage",
        description="Organize tools, dispose of old items, and sweep the garage floor",
        priority="low",
        status="pending",
        category="personal",
        due_date=timezone.now() + timedelta(days=10),
        time_tracking=False
    ),
    Task(
        title="Database optimization",
        description="Analyze and optimize slow-running database queries",
        priority="medium",
        status="completed",
        category="work",
        due_date=timezone.now() - timedelta(days=3),
        time_tracking=True
    ),
    Task(
        title="Volunteer at food bank",
        description="Help distribute meals at the local community food bank",
        priority="medium",
        status="pending",
        category="others",
        due_date=timezone.now() + timedelta(days=6),
        time_tracking=False
    ),
    Task(
        title="Read 'Clean Code' book",
        description="Complete reading the software development best practices book",
        priority="low",
        status="in-progress",
        category="personal",
        due_date=timezone.now() + timedelta(days=30),
        time_tracking=True
    ),
    Task(
        title="Team building meeting",
        description="Organize and facilitate monthly team building activities",
        priority="medium",
        status="pending",
        category="work",
        due_date=timezone.now() + timedelta(days=12),
        time_tracking=False
    ),
    Task(
        title="Plant garden vegetables",
        description="Prepare soil and plant tomatoes, peppers, and herbs in backyard garden",
        priority="low",
        status="completed",
        category="personal",
        due_date=timezone.now() - timedelta(days=5),
        time_tracking=False
    ),
    Task(
        title="Attend Python conference",
        description="Participate in PyCon 2025 and attend relevant workshops",
        priority="high",
        status="pending",
        category="others",
        due_date=timezone.now() + timedelta(days=45),
        time_tracking=True
    ),
    Task(
        title="Security audit review",
        description="Review security vulnerabilities report and implement fixes",
        priority="high",
        status="in-progress",
        category="work",
        due_date=timezone.now() + timedelta(days=4),
        time_tracking=True
    ),
    Task(
        title="Exercise routine planning",
        description="Create weekly workout schedule and meal prep plan",
        priority="medium",
        status="completed",
        category="personal",
        due_date=timezone.now() - timedelta(days=1),
        time_tracking=False
    ),
    Task(
        title="Research new technologies",
        description="Investigate emerging web frameworks and assess adoption feasibility",
        priority="low",
        status="pending",
        category="others",
        due_date=timezone.now() + timedelta(days=28),
        time_tracking=True
    )
]

# Method 1: Save all tasks individually
for task in dummy_tasks:
    task.save()

# Method 2: Bulk create (more efficient for large datasets)
# Task.objects.bulk_create(dummy_tasks)

print(f"Successfully created {len(dummy_tasks)} dummy tasks!")

# Optional: Display created tasks
print("\nCreated tasks:")
for i, task in enumerate(dummy_tasks, 1):
    print(f"{i}. {task.title} - {task.priority} priority, {task.status} status")