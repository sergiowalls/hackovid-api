from django.contrib.auth.models import AbstractUser
from django.db import models


class LearningUnit(models.Model):
    title = models.fields.CharField(max_length=140)
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


class User(AbstractUser):
    institution = models.fields.CharField(max_length=60)
    description = models.fields.CharField(max_length=255, null=True, blank=True)
    saved_sections = models.ManyToManyField(Section, blank=True)
    learning_units = models.ManyToManyField(LearningUnit, blank=True)


class SectionCreator(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)


class Class(models.Model):
    title = models.fields.CharField(max_length=120)
    sections = models.ManyToManyField(Section, blank=True)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    learning_unit = models.ForeignKey(LearningUnit, on_delete=models.DO_NOTHING, null=True)
    created_at = models.fields.DateTimeField(auto_now_add=True)


class File(models.Model):
    file = models.FileField(blank=False, null=False)

    def __str__(self):
        return self.file.name


