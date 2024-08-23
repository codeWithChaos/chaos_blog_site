from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'myBlog/login.html', context)


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'myBlog/signup.html', context)


def index(request):
    
    context = {}
    return render(request, 'myBlog/index.html', context)


def about(request):
    context = {}
    return render(request, 'myBlog/about.html', context)


def post(request):
    context = {}
    return render(request, 'myBlog/post.html', context)


def contact(request):
    context = {}
    return render(request, 'myBlog/contact.html', context)
