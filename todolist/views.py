import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from todolist.models import Task
from todolist.forms import Input_Form

@login_required(login_url='/todolist/login/')
# fungsi menampilkan task
def show_todolist(request):
    data_task_item = Task.objects.all()
    context = {
        "list_task": data_task_item,
        "task_user" : request.user
    }
    return render(request, "todolist.html", context)

# fungsi mendaftarkan pengguna
def register(request):
    # memvalidasi input
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

# fungsi melakukan login
def login_user(request):
    # memvalidasi input
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # melakukan login terlebih dahulu
            login(request, user)
            
            # membuat respons
            response = HttpResponseRedirect(reverse("todolist:show_todolist"))
            
            # membuat cookie last_login dan menambahkannya ke dalam response
            response.set_cookie('last_login', str(datetime.datetime.now())) 
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)
    
# fungsi melakukan logout
def logout_user(request):
    logout(request)
    
    # mengembalikan ke halaman awal dan menghapus cookie last_login
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

# fungsi membuat task
def create_task(request):
    # memvalidasi input
    if request.method == 'POST':
        task_form = Input_Form(request.POST)
        if task_form.is_valid():
            task_user = request.user
            task_date = datetime.date.today()
            task_title = request.POST.get('title')
            task_description = request.POST.get('description')
            
            # membuat objek baru berdasarkan model dan menyimpannya ke database
            new_task = Task(user=task_user, date=task_date.strftime("%Y-%m-%d"), title=task_title, description=task_description)
            new_task.save()
            
            # mengembalikan ke halaman yang menampilkan tasks
            data_task_item = Task.objects.all()
            context = {
                "list_task": data_task_item,
                "task_user" : request.user
            }
            return render(request, 'todolist.html', context)  
        else:
            task_form = Input_Form()
    return render(request, 'create-task.html')  