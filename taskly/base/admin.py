from django.contrib import admin
from .models import sample, task

# Register your models here.
models_list = [sample,]
for i in models_list:
    pass
admin.site.register(task)
admin.site.register(sample)
