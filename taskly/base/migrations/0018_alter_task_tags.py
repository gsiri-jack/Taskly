# Generated by Django 4.2.20 on 2025-05-01 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0017_alter_task_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='tags',
            field=models.ManyToManyField(default='', null=True, to='base.tag'),
        ),
    ]
