from django.http.request import split_domain_port
from django_filters.rest_framework import DjangoFilterBackend, FilterSet, NumberFilter
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView, ListAPIView
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView

from hackovid import settings
from learning.models import Class, LearningUnit, User, \
    Section
from learning.serializers import UserCreateSerializer, UserSerializer, ClassCreateSerializer, ClassSerializer, \
    LearningUnitSerializer, SectionsSerializer, FileSerializer


class ClassFilter(FilterSet):
    learning_unit = NumberFilter(field_name='sections__learning_unit')
    teacher = NumberFilter(field_name='teacher')


class ClassesView(ListCreateAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ClassFilter

    def post(self, request, *args, **kwargs):
        data = request.data
        data['teacher'] = request.user.pk
        serializer = ClassCreateSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClassView(RetrieveUpdateDestroyAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer


class LearningUnitsView(ListCreateAPIView):
    queryset = LearningUnit.objects.all()
    serializer_class = LearningUnitSerializer


class LearningUnitView(RetrieveUpdateDestroyAPIView):
    queryset = LearningUnit.objects.all()
    serializer_class = LearningUnitSerializer


class UsersView(APIView):

    def post(self, request):
        learning_units = request.data.pop('learning_units')
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            for learning_unit in learning_units:
                user.learning_units.add(learning_unit)
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MyUserView(APIView):

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class MySavedSectionsView(ListAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionsSerializer

    def get_serializer_context(self):
        return {'user': self.request.user}

    def get_queryset(self):
        return self.request.user.saved_sections


class MyClassesView(ListAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer

    def get_serializer_context(self):
        return {'user': self.request.user}

    def get_queryset(self):
        return self.request.user.class_set


class MySavedSectionView(APIView):

    def post(self, request, pk):
        request.user.saved_sections.add(pk)
        request.user.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class MyLearningUnitsView(ListAPIView):
    queryset = LearningUnit.objects.all()
    serializer_class = LearningUnitSerializer

    def get_serializer_context(self):
        return {'user': self.request.user}

    def get_queryset(self):
        return self.request.user.learning_units


class FileUploadView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request):
        file_serializer = FileSerializer(data=request.data)

        if file_serializer.is_valid():
            file = file_serializer.save()
            host = request.get_host()
            domain, _ = split_domain_port(host)
            port = request.get_port()
            file_url = "http://{0}:{1}{2}{3}".format(domain, port, settings.MEDIA_URL, file)
            return Response({'url': file_url}, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
