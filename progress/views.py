from django.shortcuts import render, get_object_or_404
from progress.models import Task, Course

def task_list(request, course_id, user_id):
    hide_completed = request.GET.get('hide_completed', 'false') == 'true'

    # Get the course
    course = get_object_or_404(Course, pk=course_id)

    # Fetch the tasks to display on the page
    tasks = Task.objects.filter(course__course_id=course_id, user_id=user_id).order_by('sort_order')
    # Show only incomplete tasks
    if hide_completed:
        tasks = tasks.filter(completed=False)  
    
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

    return render(request, 'progress/tasks.html', {
        'tasks': tasks, 
        'user_id': user_id,
        'course_code': course.short_code,
        'hide_completed': hide_completed
        })
