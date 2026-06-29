from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializer import*

class BookView(ModelViewSet):

    queryset=Book.objects.all()
    serializer_class=Book_Serializer