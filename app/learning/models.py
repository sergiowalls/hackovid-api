from django.contrib.auth.models import User
from django.db import models
from rest_framework import serializers


class LearningUnit(models.Model):
    title = models.fields.CharField(max_length=60)
    subject = models.fields.CharField(max_length=60)
    course = models.fields.CharField(max_length=60)


class Resource(models.Model):
    title = models.fields.CharField(max_length=60)


class LinkResource(Resource):
    link = models.fields.URLField()
    is_video = models.fields.BooleanField()


class Section(models.Model):
    title = models.fields.CharField(max_length=60)
    description = models.fields.TextField()
    resources = models.ManyToManyField(Resource, blank=True)


class Class(models.Model):
    title = models.fields.CharField(max_length=120)
    learning_unit = models.ForeignKey(LearningUnit, on_delete=models.DO_NOTHING)
    sections = models.ManyToManyField(Section, blank=True)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.fields.DateTimeField(auto_now_add=True)


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = '__all__'
