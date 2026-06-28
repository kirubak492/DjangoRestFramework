from django.db import models

# Create your models here.
class Students(models.Model):

    name=models.CharField(max_length=50)
    age=models.IntegerField(default=10)

    def __str__(self):
        return (self.name + " "+str(self.age)) 
    

class Task(models.Model):
    taskName=models.CharField(max_length=50)
    description=models.TextField()