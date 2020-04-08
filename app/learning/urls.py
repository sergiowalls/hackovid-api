from django.urls import path

from learning import views

urlpatterns = [
    path(r'', views.ClassView.as_view()),
]
