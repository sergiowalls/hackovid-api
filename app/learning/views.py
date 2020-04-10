from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from learning.models import Class, ClassSerializer, UserSerializer, LearningUnit, LearningUnitSerializer


class ClassesView(ListCreateAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer


class ClassView(RetrieveUpdateDestroyAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer

class LearningUnitsView(ListCreateAPIView):
    queryset = LearningUnit.objects.all()
    serializer_class = LearningUnitSerializer

class LearningUnitView(RetrieveUpdateDestroyAPIView):
    queryset = LearningUnit.objects.all()
    serializer_class = LearningUnitSerializer


class UserView(APIView):

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            save = serializer.save()
            print(save)
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
