from django.shortcuts import render
from progress.models import Task

def task_list(request, week_num, user_id):
    # Fetch the tasks to display on the page
    tasks = Task.objects.filter(week_num=week_num, user_id=user_id).order_by('sort_order')
    
    if request.method == 'POST':
        # Loop through the tasks and update their state based on the form data
        for task in tasks:
            # Check if the task checkbox was ticked
            completed = f'task_{task.id}' in request.POST
            # Get the comment for this task
            comment = request.POST.get(f'comment_{task.id}', '')
            # Update the task
            task.completed = completed
            task.comment = comment
            task.save()

    return render(request, 'progress/tasks.html', {'tasks':tasks, 'user_id':user_id})
