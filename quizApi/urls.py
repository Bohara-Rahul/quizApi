from django.urls import path

from .views import post_quizzes

urlpatterns = [
  path('lesson/<int:lessonId>/question/<int:questionId>', post_quizzes)
]