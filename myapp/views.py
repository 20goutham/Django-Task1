from django.shortcuts import render
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse('Hello world')

def task_view(request):
    context = {
        'title': 'Welcome to the Task Page',
        'description': '> Thanks to O(1) for teaching me Django.\n> I am learning a lot!\n> This is fun!'
    }
    
    return render(request, 'task.html',context)