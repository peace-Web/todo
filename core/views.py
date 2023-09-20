from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm, UserForm
from django.contrib.auth.models import User, auth
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

def register(request):
    register_form = UserForm()
    if request.method == "POST":
        register_form = UserForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            return redirect("login_view")
    context = {"form": register_form}
    return render(request, 'core/register.html', context)

def loginView(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username = username, password = password)
        if user is not None:
            print("valid")
            login(request, user)
            return redirect('home')
        else:
            print("Invalid")
            messages.warning(request, "username or password incorrect!")
    return render(request, 'core/login.html')

def logoutView(request):
    auth.logout(request)
    return redirect("/")

@login_required()
def home(request):
    if request.user.is_authenticated:

        user = request.user
        task = Task.objects.filter(user = user)
        
        
        form = TaskForm()
         
        if request.method == "POST":
            print("Yes")
            form = TaskForm(request.POST)
            form.instance.user = user
            if form.is_valid():
               form.save()
            else:
                print(form.errors.as_data())
            return redirect("/")
        context = {"task": task, "form": form}
    return render(request, 'core/home.html', context)


@login_required()
def edit(request, pk):
    task = Task.objects.get(id = pk)
    form = TaskForm(instance=task)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("/")
    context = {"task": task, "form": form}
    return render(request, 'core/edit.html', context)


@login_required()
def delete(request, pk):
    task = Task.objects.get(id = pk)
    if request.method == "POST":
        task.delete()
        return redirect("/")
    context = {"task": task}
    return render(request, 'core/delete.html', context)