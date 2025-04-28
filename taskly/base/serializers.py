from django.db import models
from rest_framework import serializers
from .models import sample, task


class SampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = task
        fields = '__all__'
