from django.db import models
from rest_framework import serializers
from .models import sample


class SampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = sample
        fields = '__all__'
