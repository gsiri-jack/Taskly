from django.shortcuts import render
from django.http import HttpResponse
from .models import sample
from .serializers import SampleSerializer
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def index(request):
    data = sample.objects.all()
    serialize = SampleSerializer(data, many=True)
    return HttpResponse(serialize)


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
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return render(request, 'base/index.html', {'title': 'Dashboard'})
            else:
                context['error'] = "Invalid username or password"
    return render(request, 'base/login.html', context)
