import csv
import os
import django

# Setup Django environment (Only needed if running as standalone script)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tracker.settings")
django.setup()

from progress.models import Course, Task

def load_courses(csv_file_path):
    """Load course data from CSV file."""
    with open(csv_file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            Course.objects.create(
                course_id=row['course_id'],  
                course_code=row['course_code'],  
                description=row['description']
            )
    print("Courses loaded successfully!")

def load_tasks(csv_file_path):
    """Load task data from CSV file."""
    with open(csv_file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            Task.objects.create(
                course_id=row['course'],  # ForeignKey reference
                user_id=row['user'],
                sort_order=row['sort_order'],
                title=row['title'],
                completed=row['completed'].lower() == 'true',  # Convert text to Boolean
                comment=row['comment']
            )
    print("Tasks loaded successfully!")

if __name__ == "__main__":
    # Adjust paths if needed
    course_csv = "data/courses.csv"
    task_csv = "data/tasks.csv"

    load_courses(course_csv)
    load_tasks(task_csv)
