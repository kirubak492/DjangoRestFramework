from django.urls import path
from .views import StudentApi, TaskViewApi,TaskViewById

urlpatterns = [
    path('details/', StudentApi.as_view()),
    path('details/<int:studentId>/',StudentApi.as_view()),
    path('task/',TaskViewApi.as_view()),
    path('task/<int:TaskId>/',TaskViewById.as_view())
    
]