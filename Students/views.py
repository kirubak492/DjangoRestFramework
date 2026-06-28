from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Students,Task
from .serializer import Task_Serializer

class StudentApi(APIView):


    def post(self,request):

        print(request.data)
        data=request.data

        newStudent=Students(name=data['name'],age=data['age'])
        newStudent.save()

        return Response ("Post api called..!!!")
    
    def get(self,request):

        student=Students.objects.all()

        stdList=[]

        for s in student:
            studentDict={
                'id':s.id,
                'name': s.name,
                'age' : s.age
            }
            stdList.append(studentDict)

        return Response(stdList)

    def put(self,request,studentId):

        data=request.data
        studentData=Students.objects.filter(id=studentId)
        studentData.update(name=data['name'],age=data['age'])
    
        return Response("Data updated succesfully")
    
    def delete(self, request, studentId):

        studentData=Students.objects.get(id=studentId)
        studentData.delete()

        return Response("Data deleted succesfully")
    
class TaskViewApi(APIView):

    def get(self,request):

        allTask=Task.objects.all()

        taskData=Task_Serializer(allTask,many=True).data

        return Response(taskData)

    def post(self,request):
        new_task=Task_Serializer(data=request.data)

        if new_task.is_valid():
            new_task.save()
            return Response ("New Task added")
        else:
            return Response(new_task.errors)
        
class TaskViewById(APIView):

    def get(self,request,TaskId):

        allTask=Task.objects.get(id=TaskId)

        taskData=Task_Serializer(allTask).data

        return Response(taskData)
    
    def put(self,request,TaskId):

        task=Task.objects.get(id=TaskId)

        taskData=Task_Serializer(task,data=request.data,partial=True)

        if taskData.is_valid():
            taskData.save();

        return Response("Task data updated")
    
    def delete(self,request,TaskId):
        
        task =Task.objects.get(id=TaskId)

        task.delete()

        return Response("Task deleted successfully")