from django.urls import path

from learning import views

urlpatterns = [
    path(r'class', views.ClassesView.as_view()),
    path(r'class/<int:pk>/', views.ClassView.as_view())
]
