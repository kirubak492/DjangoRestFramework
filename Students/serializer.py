from rest_framework.serializers import ModelSerializer
from .models import Task    

# we can write one or more serializer for one model
class Task_Serializer(ModelSerializer):

    #Meta class is used for write the serialization for which model
    class Meta: 

        model=Task
        fields='__all__'

