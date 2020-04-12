from django.contrib.auth.models import AbstractUser
from django.db import models
from rest_framework import serializers


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
    learning_unit = models.ForeignKey(LearningUnit, on_delete=models.DO_NOTHING)


class User(AbstractUser):
    institution = models.fields.CharField(max_length=60)
    description = models.fields.CharField(max_length=255, null=True, blank=True)
    saved_sections = models.ManyToManyField(Section, blank=True)
    learning_units = models.ManyToManyField(LearningUnit, blank=True)


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'institution', 'first_name']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data.get('password'))
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.set_password(validated_data.get('password'))
        instance.save()
        return instance


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'id', 'institution', 'first_name']


class SectionCreator(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)


class Class(models.Model):
    title = models.fields.CharField(max_length=120)
    sections = models.ManyToManyField(Section, blank=True)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.fields.DateTimeField(auto_now_add=True)


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'


class ClassPostSerializer(serializers.ModelSerializer):
    sections = SectionSerializer(many=True)

    class Meta:
        model = Class
        fields = '__all__'

    def create(self, validated_data):
        sections = validated_data.pop('sections')
        class_ = Class.objects.create(**validated_data)
        for section_data in sections:
            resources = section_data.pop('resources')
            section = Section.objects.create(**section_data)
            class_.sections.add(section)
        class_.save()
        return class_


class ClassSerializer(serializers.ModelSerializer):
    sections = SectionSerializer(many=True)
    teacher = UserSerializer()

    class Meta:
        model = Class
        fields = '__all__'


class LearningUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = LearningUnit
        fields = '__all__'


class SectionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'


class File(models.Model):
    file = models.FileField(blank=False, null=False)

    def __str__(self):
        return self.file.name

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = "__all__"

