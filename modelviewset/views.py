from django.shortcuts import render
from modelserializor.serializers import StudentSerializer
from modelserializor.models import Student_Table
from rest_framework import viewsets
# Create your views here.
#All Operations can be done by single class
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset=Student_Table.objects.all()
    serializer_class=StudentSerializer

#Only Read Operations can be done->Read and Retreive
class StudentReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset=Student_Table.objects.all()
    serializer_class=StudentSerializer
