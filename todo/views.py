from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Todo
# Create your views here.

def user_login(request):

    if request.session.has_key('is_logged'):
        return redirect('dashboard')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user_check = authenticate(username=username, password=password)
        if user_check is not None:
            login(request, user_check)
            request.session['is_logged'] = True
            messages.add_message(request, messages.SUCCESS, 'You successfully logged In')
            return redirect('dashboard')
        else:
            messages.add_message(request, messages.WARNING, 'Try real something')

    return render(request, 'login.html')


def signup(request):
    if request.session.has_key('is_logged'):
        return redirect('dashboard')

    if request.method == 'POST':
        cheek_username = request.POST.get('username')
        if User.objects.filter(username=cheek_username):
            messages.add_message(request, messages.WARNING, 'Username Already Taken.')
            return redirect('signup')
        else:
            if request.POST.get('password') == request.POST.get('confirm_password'):
                fname = request.POST.get('first_name')
                lname = request.POST.get('last_name')
                username = request.POST.get('username')
                email = request.POST.get('email')
                password = request.POST.get('password')

                user_creawte = User.objects.create_user(first_name=fname, last_name=lname, username=username, password=password, email=email)
                user_creawte.save()


                messages.add_message(request, messages.SUCCESS, 'Account Create successfully')
                return redirect('login')


            else:
                messages.add_message(request, messages.ERROR, 'Your password & confirm password was not match')
                return redirect('signup')

    return render(request, 'signup.html')



def user_logout(request):
    logout(request)
    messages.add_message(request, messages.SUCCESS, 'You have Successfully Logout')
    return redirect('login')



def dashboard(request):
    if request.session.has_key('is_logged'):

        if request.method == 'POST':
            title = request.POST.get('title')
            decs = request.POST.get('decs')
            creator = request.user

            todo_create = Todo.objects.create(creator=creator, title=title, decs=decs)
            todo_create.save()

            messages.add_message(request, messages.SUCCESS, 'Todo Added Successfuly')


        view_todo = Todo.objects.filter(creator__username=request.user)[::-1]

        data = {
            'view_todo': view_todo,
        }

        return render(request, 'dashboard.html', context=data)
    else:
        messages.add_message(request, messages.WARNING, 'Login First...')
        return redirect('login')


def single_view(request, id):
    if request.session.has_key('is_logged'):
        todo_view = Todo.objects.filter(pk=id)
        data = {
            'todo_view': todo_view,
        }
        return render(request, 'single_todo_view.html', context=data)
    else:
        messages.add_message(request, messages.WARNING, 'Login First')
        return redirect('login')


def delete_todo(request, id):
    if request.session.has_key('is_logged'):
        delete_todo = Todo.objects.filter(pk=id)
        delete_todo.delete()
        return redirect('dashboard')
    else:
        messages.add_message(request, messages.WARNING, 'Login First')
        return redirect('login')