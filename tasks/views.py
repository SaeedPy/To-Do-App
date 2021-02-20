from django.shortcuts import render, redirect

from .models import Tasks
from .forms import TasksForm
from django.contrib import messages


def home(request):
	tasks = Tasks.objects.all()

	form = TasksForm()
	if request.method == 'POST':
		form = TasksForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('home')	

	context = {'tasks': tasks,
				'form': form}
	return render(request, 'tasks/home.html', context)


def deleteTask(request, pk):
	task = Tasks.objects.get(pk=pk)

	if request.method == 'POST':
		task.delete()
		messages.info(request, 'Task Is Deleted!!')
		return redirect('home')

	context = {'task': task}

	return render(request, 'tasks/delete.html', context)


def updateTask(request, pk):
	task = Tasks.objects.get(pk=pk)

	form = TasksForm(instance=task)
	if request.method == 'POST':
		form = TasksForm(data=request.POST, instance=task)
		if form.is_valid():
			form.save()
			messages.info(request, 'Task Is Updated!')
			return redirect('home')

	context = {'task': task,
				'form': form}
	return render(request, 'tasks/update.html', context)