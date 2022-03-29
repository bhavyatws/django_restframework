from django.shortcuts import render
from modelserializor.serializers import StudentSerializer

from api.models import Student
from rest_framework.generics import ListAPIView,CreateAPIView,UpdateAPIView,RetrieveAPIView,DestroyAPIView,ListCreateAPIView,RetrieveDestroyAPIView,RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView
# Create your views here.
#Concrete View

#Get all student
class StudentList(ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

#Create Student
class StudentCreate(CreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
#Retreive
class StudentRetreive(RetrieveAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
#update Student
class StudentUpdate(UpdateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
#Delete Student
class StudentDelete(DestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

#ListCreateView
class StudentListCreate(ListCreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

#RetreiveDestroy
class StudentRetrieveDestroy(RetrieveDestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

#RetreiveUpdate
class StudentRetrieveUpdate(RetrieveUpdateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

#RetreiveUpdateDestroy=>Destory means delete
class StudentRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
#Only using two ListCreateAPIView and RetrieveUpdateDestroyAPIView CRUD can be made