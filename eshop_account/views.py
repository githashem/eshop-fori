from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from . import forms


def login_user(request):
    if request.user.is_authenticated:
        return redirect("/")

    login_form = forms.LoginForm(request.POST or None)
    if login_form.is_valid():
        username = login_form.cleaned_data.get("username")
        password = login_form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is None:
            login_form.add_error('username', 'کاربری با این مشخصات پیدا نشد.')
        else:
            login(request, user)
            return redirect('/')
    context = {
        'login_form': login_form
    }
    return render(request, 'account/login.html', context=context)


def register(request):
    if request.user.is_authenticated:
        return redirect("/")

    register_form = forms.RegisterForm(request.POST or None)
    if register_form.is_valid():
        username = register_form.cleaned_data.get("username")
        email = register_form.cleaned_data.get("email")
        password = register_form.cleaned_data.get("password")
        User.objects.create_user(username=username, email=email, password=password)
        return redirect('/login')

    context = {
        'register_form': register_form
    }
    return render(request, 'account/register.html', context=context)


def logout_user(request):
    logout(request)
    return redirect("/login")


@login_required(login_url='/login')
def dashboard_page(request):
    return render(request, 'account/dashboard.html', {})


@login_required(login_url='/login')
def edit_dashboard_page(request):
    user = User.objects.get(id=request.user.id)
    edit_user_form = forms.UserEditForm(request.POST or None, initial={'first_name': user.first_name, 'last_name': user.last_name})
    if edit_user_form.is_valid():
        user.first_name = edit_user_form.cleaned_data.get('first_name')
        user.last_name = edit_user_form.cleaned_data.get('last_name')
        user.save()
    return render(request, 'account/dashboard-edit.html', {'edit_user_form': edit_user_form})
