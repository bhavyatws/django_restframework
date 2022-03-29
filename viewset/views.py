
from django.shortcuts import render
from modelserializor.serializers import StudentSerializer
from modelserializor.models import Student_Table
from rest_framework.generics import ListAPIView,CreateAPIView,UpdateAPIView,RetrieveAPIView,DestroyAPIView,ListCreateAPIView,RetrieveDestroyAPIView,RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
# Create your views here.
#Using ViewSet
#Advantage of ViewSet => it generate all routes automatically



#Create Student
class StudentViewSet(viewsets.ViewSet):
    #all student 
    def list(self,request):
        print("******List**************")
        print("Basename:",self.basename)
        print("Action:",self.action)
        print("Detail:",self.detail)
        print("Suffix:",self.suffix)
        print("Description:",self.description)
        print("Name:",self.name)
        stu=Student_Table.objects.all()
        serializer=StudentSerializer(stu,many=True)
        return Response(serializer.data)
    
    #fetching particular student
    def retrieve(self,request,pk=None):
        id=pk
        if id is not None:
            stu=Student_Table.objects.get(id=id)
            serializer=StudentSerializer(stu)
            return Response(serializer.data)
    #create student
    def create(self,request):
        #request.data fetch all data from form i.e serializer or json id drf
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def update(self,request,pk):
        id=pk
        stu=Student_Table.objects.get(id=id)
        serializer=StudentSerializer(stu,data=request.data)#request.data vaneko update ko lagi data ho
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Data Updated'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self,request,pk):
        id=pk
        stu=Student_Table.objects.get(id=id)
        serializer=StudentSerializer(stu,data=request.data,partial=True)#request.data vaneko update ko lagi data ho
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial Data Updated'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        id=pk
        stu=Student_Table.objects.get(id=id)
        stu.delete()
        return Response({'msg':'Data Deleted'})