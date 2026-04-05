from django.shortcuts import render
from .models import Task
from django.contrib.auth.decorators import login_required

# @login_required
def tasks(request):
    if request.method == "POST":
        data = request.POST
        new_task = Task.objects.create(
            title = data.get('title'),
            description = data.get('description'),
            user = request.user
        )
        context = {'tasks': new_task}
        return render(request, 'tasks/add-task.html', context)
    
    tasks = Task.objects.filter(user=request.user).order_by('-date_created')
    context = {'tasks': tasks}
    print(context)
    return render(request, 'tasks/add-task.html', context)