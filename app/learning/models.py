from django.db import models
from rest_framework import serializers


class Class(models.Model):
    title = models.fields.CharField(max_length=120, blank=False, null=False)
    created_at = models.fields.DateTimeField(auto_now_add=True)


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = '__all__'
