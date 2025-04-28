from django.contrib import admin
from .models import sample, task

# Register your models here.
models_list = [sample, task]
for i in models_list:
    admin.site.register(i)
