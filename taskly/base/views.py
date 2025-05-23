from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse
from .models import sample,  tag, task, task_tag_link
from .serializers import SampleSerializer
from .forms import LoginForm, task_creation_form
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def index(request):
    data = task.objects.all()
    tag_data = tag.objects.all()
    username = request.session.get('username')
    task_create = task_creation_form()
    return render(request, 'base/index.html', {'title': 'Dashboard', 'tasks': data, 'username': username, "task_create": task_create, 'tags': tag_data})


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
    task_data = task.objects.get(id=id)
    # task_data = sample.objects.all(id=id)
    username = request.session.get('username')
    print(username)

    return render(request, 'base/task_detail.html', {'task': task_data, 'username': username})


def create_task(request):
    if request.method == 'POST':
        form = task_creation_form(request.POST)

        title = request.POST['task_title']
        desc = request.POST['task_description']
        due_date = request.POST['due_date']
        task_tag = request.POST['task_tag']  # Assuming this is the tag name
        task_priority = request.POST['task_priority']

        # Create the task instance
        new_task = task.objects.create(
            title=title,
            description=desc,
            user=request.user,
            due_date=due_date,
            priority=task_priority
        )

        # Handle the tag
        try:
            tag_instance = tag.objects.get(tag_name=task_tag)
        except tag.DoesNotExist:
            # Option 1: Create a new tag if it doesn't exist
            tag_instance = tag.objects.create(
                tag_name=task_tag, user=request.user)

        # Add the tag to the task instance
        new_task.tags.add(tag_instance)

        print('Task created successfully')
        return redirect('index')


def delete_task(request, id):
    product = task.objects.get(id=id)
    # product = sample.objects.get(id=id)
    product.delete()
    return redirect('index')


def get_task_tags(request, id):
    task_instance = get_object_or_404(task, id=id)
    tags = task_instance.tags.all()
    tag_list = [tag.tag_name for tag in tags]
    print(tag_list)
    return JsonResponse({'tags': tag_list})
# views.py


def update_task(request, id):
    task_ins = get_object_or_404(task, id=id)
    # task_ins = get_object_or_404(sample, id=id)
    if request.method == 'POST':
        form = task_creation_form(request.POST, instance=task_ins)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
    else:
        form = task_creation_form(instance=task_ins)
    return render(request, 'base/update_task.html', {'form': form, 'task': task_ins})


@csrf_exempt
def toggle_task(request):
    if request.method == 'POST':
        task_id = request.POST.get('task_id')
        task_ins = task.objects.get(id=task_id)
        task_ins.completed = not task_ins.completed
        task_ins.save()
        print("TASK", task_ins.completed)
        return JsonResponse({'success': True, 'completed': task_ins.completed})
    return JsonResponse({'success': False}, status=400)


def create_task_form(request):
    tags = tag.objects.all()
    return render(request, 'base/create_task_form.html', {'tags': tags})


def add_label(request):
    tags = tag.objects.all()
    return render(request, 'base/add_tag.html', {'tags': tags})
