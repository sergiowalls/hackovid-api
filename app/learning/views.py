from django_filters.rest_framework import DjangoFilterBackend, FilterSet, NumberFilter
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from learning.models import Class, ClassSerializer, UserSerializer, LearningUnit, LearningUnitSerializer, User, \
    ClassPostSerializer, UserCreateSerializer


class ClassFilter(FilterSet):
    learning_unit = NumberFilter(field_name='sections__learning_unit')


class ClassesView(ListCreateAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ClassFilter

    def post(self, request, *args, **kwargs):
        data = request.data
        data['teacher'] = request.user.pk
        serializer = ClassPostSerializer(data=data)
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
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MyUserView(APIView):

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)


class UserView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
