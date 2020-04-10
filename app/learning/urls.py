from django.urls import path

from learning import views
from learning.views import LearningUnitsView, LearningUnitView

urlpatterns = [
    path(r'user', views.UserView.as_view()),
    path(r'class', views.ClassesView.as_view()),
    path(r'class/<int:pk>/', views.ClassView.as_view()),
    path(r'learning-units', views,LearningUnitsView.as_view()),
    path(r'learning-units/<int:pk>/', views,LearningUnitView.as_view())
]
