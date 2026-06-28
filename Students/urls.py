from django.urls import path
from .views import StudentApi, TaskViewApi

urlpatterns = [
    path('details/', StudentApi.as_view()),
    path('details/<int:studentId>/',StudentApi.as_view()),
    path('task/',TaskViewApi.as_view()),
    path('task/<int:taskId>/',TaskViewApi.as_view()),
    
]