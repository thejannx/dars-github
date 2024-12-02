from django.shortcuts import render
from .models import Task

def task_list(request):

    title = request.GET.get('title')
    description = request.GET.get('description')
    is_completed = request.GET.get('is_completed')


    if title and description and is_completed is not None:
        try:
            Task.objects.create(
                title=title,
                description=description,
                is_completed=(is_completed.lower() == 'true')  # Convert string to boolean
            )
        except Exception as e:
            print(f"Error creating task: {e}")  # Optionally log the error


    tasks = Task.objects.all()


    ctx = {'tasks': tasks}

    return render(request, 'tasks/task_list.html', ctx)
