from django.contrib import admin
from .models import sample, task, tag, task_tag_link

# Register your models here.
models_list = [sample, task, tag, task_tag_link]
for i in models_list:
    pass
admin.site.register(task)
admin.site.register(sample)
admin.site.register(tag)
admin.site.register(task_tag_link)
