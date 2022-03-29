from django.shortcuts import render
from modelserializor.serializers import StudentSerializer
from modelserializor.models import Student_Table
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.
#All Operations can be done by single class
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset=Student_Table.objects.all()
    serializer_class=StudentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]