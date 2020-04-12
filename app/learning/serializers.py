from rest_framework import serializers

from learning.models import User, Section, Class, LearningUnit, File


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


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'


class ClassCreateSerializer(serializers.ModelSerializer):
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


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = "__all__"