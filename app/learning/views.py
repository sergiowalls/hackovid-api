from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from learning.models import Class, ClassSerializer


class ClassesView(ListCreateAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer


class ClassView(RetrieveUpdateDestroyAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
