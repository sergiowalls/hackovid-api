from django.urls import path

from learning import views

urlpatterns = [
    path(r'users', views.UserView.as_view()),
    path(r'classes', views.ClassesView.as_view()),
    path(r'classes/<int:pk>/', views.ClassView.as_view()),
    path(r'learning-units', views.LearningUnitsView.as_view()),
    path(r'learning-units/<int:pk>/', views.LearningUnitView.as_view())
]
