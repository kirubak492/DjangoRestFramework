from rest_framework.serializers import ModelSerializer
from .models import *

class Book_Serializer(ModelSerializer):

    class Meta:

        model=Book
        fields='__all__'