from ast import arg
from django.shortcuts import render
from api.models import Student
from .serializers import StudentSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,DestroyModelMixin,UpdateModelMixin
# Create your views here.
#List Student
class StudentList(GenericAPIView,ListModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

    def get(self,request,*args, **kwargs):
        return self.list(request,*args,**kwargs)

#create students
class CreateStudent(GenericAPIView,CreateModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

    def post(self,request,*args, **kwargs):
        return self.create(request,*args,**kwargs)

#Retreive students=>fetch particular data like detail
class RetrieveStudent(GenericAPIView,RetrieveModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

    def get(self,request,*args, **kwargs):
        return self.retrieve(request,*args,**kwargs)

#Update student's data
class UpdateStudent(GenericAPIView,UpdateModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

    def put(self,request,*args, **kwargs):#put and patch both will work here
        return self.update(request,*args,**kwargs)
#Delete student data
class DeleteStudent(GenericAPIView,DestroyModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

    def delete(self,request,*args, **kwargs):
        return self.destroy(request,*args,**kwargs)

#Comining list and create as no pk is required for do that
class List_OR_CreateStudentAPI(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

    def get(self,request,*args, **kwargs):
        return self.list(request,*args,**kwargs)
    
    def post(self,request,*args, **kwargs):
        return self.create(request,*args,**kwargs)

#Combining Retrieve,Update and Delete as pk is required
class Retrieve_Update_Delete_API(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    #retreive
    def get(self,request,*args, **kwargs):
        return self.retrieve(request,*args,**kwargs)
    #update
    def put(self,request,*args, **kwargs):#put and patch both will work here
        return self.update(request,*args,**kwargs)
    #delete
    def delete(self,request,*args, **kwargs):
        return self.destroy(request,*args,**kwargs)