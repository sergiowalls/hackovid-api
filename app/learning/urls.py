from django.urls import path

from learning import views

urlpatterns = [
    path(r'user', views.UserView.as_view()),
    path(r'class', views.ClassesView.as_view()),
    path(r'class/<int:pk>/', views.ClassView.as_view()),
    path(r'learning-unit', views.LearningUnitsView.as_view()),
    path(r'learning-unit/<int:pk>/', views.LearningUnitView.as_view())
]
