import datetime
from todolist.models import Task
from django import forms
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse

class NewForms(forms.Form):
    title = forms.CharField(label="Title")
    description = forms.CharField(label="Description", widget=forms.Textarea)

@login_required(login_url='/todolist/login/')
def show_todolist(request):
    details = Task.objects.filter(user=request.user)
    context = {
    'todo_details': details,
    'last_login': request.COOKIES['last_login'],
    }
    return render(request, "todolist.html", context)

@login_required(login_url='/todolist/login/')
def add_activity(request):
    if request.method == "POST":
        forms = NewForms(request.POST)
        if forms.is_valid():
            new_task = Task(
                user = request.user,
                title = forms.cleaned_data["title"],
                description = forms.cleaned_data["description"],
            )
            new_task.save()
            return redirect("todolist:show_todolist")

    forms = NewForms()
    context={"form":forms}
    return render(request, "addtask.html", context)

@login_required(login_url='/todolist/login/')
def status(request, id):
    target = Task.objects.get(pk=id)
    target.is_finished = not(target.is_finished)
    target.save()
    return redirect("todolist:show_todolist")

@login_required(login_url='/todolist/login/')
def delete(request, id):
    Task.objects.get(id=id).delete()
    return redirect("todolist:show_todolist")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("todolist:show_todolist"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response