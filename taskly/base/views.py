from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse
from .models import sample
from .serializers import SampleSerializer
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def index(request):
    data = sample.objects.all()
    serialize = SampleSerializer(data, many=True)
    username = request.session.get('username')
    return render(request, 'base/index.html', {'title': 'Dashboard', 'tasks': serialize.data, 'username': username})


def user_login(request):
    context = {
        'title': 'Login',
        'form': LoginForm(),
    }
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            request.session["username"] = username
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse(index), {'title': 'Dashboard', 'username': username})
            else:
                context['error'] = "Invalid username or password"
    return render(request, 'base/login.html', context)


def task_detail(request, id):
    task = sample.objects.get(id=id)
    username = request.session.get('username')
    print(username)

    return render(request, 'base/task_detail.html', {'task': task, 'username': username})


def create_task(request):
    print('Jack')
    return redirect('index')
