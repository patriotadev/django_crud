from django.shortcuts import redirect, render
from .models import todoData
from django.shortcuts import render, redirect
from django.urls import reverse
# --
from django.http import HttpResponse
from django.core import serializers
# Create your views here.


def index(request):
    todos = todoData.objects.all().order_by('-id')
    # serialized_todo = serializers.serialize('python', todo)
    # return JsonResponse(serialized_todo, safe=False)
    return render(request, 'todo/index.html', {'todos': todos})


def add(request):
    title = request.POST['title']
    todo = todoData(title=title, done=False)
    todo.save()
    return redirect(reverse('index'))


def update(request, id):
    todo = todoData.objects.get(id=id)
    todo.done = not todo.done
    todo.save()
    return redirect(reverse('index'))


def delete(request, id):
    todo = todoData.objects.get(id=id)
    todo.delete()
    return redirect(reverse('index'))
