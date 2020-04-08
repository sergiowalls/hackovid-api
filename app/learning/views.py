from rest_framework.generics import ListCreateAPIView

from learning.models import Class, ClassSerializer


class ClassView(ListCreateAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
