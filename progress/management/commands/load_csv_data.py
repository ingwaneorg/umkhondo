import csv
from django.core.management.base import BaseCommand
from progress.models import Task
import os 

class Command(BaseCommand):
    help = 'Load tasks from a CSV file'

    def handle(self, *args, **kwargs):
       # Get the path to the CSV file in the data directory
        csv_file_path = os.path.join(os.getcwd(), 'data', 'tasks.csv')
        
        with open(csv_file_path, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Create Task objects from CSV data
                Task.objects.create(
                    course_code=row['course'],
                    user_id=row['user'],
                    sort_order=row['sort_order'],
                    title=row['title'],
                    completed=row['completed'] == 'True',
                    comment=row['comment']
                )
        self.stdout.write(self.style.SUCCESS('Successfully loaded tasks from CSV!'))
