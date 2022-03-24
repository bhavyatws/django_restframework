from functools import partial
import json
from unicodedata import name
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
import io
from rest_framework.parsers import JSONParser
from api import serializers
#Fro Class Base View
from django.utils.decorators import method_decorator
from django.views import  View

# Create your views here.
#Model Object-Single Student Data
def student_detail(request,pk):
    stu=Student.objects.get(id=pk)
    print(stu)
    serializer=StudentSerializer(stu)#serializing data
    print("Serializer ",serializer)
    print("Serializer Data:",serializer.data)
    json_data=JSONRenderer().render(serializer.data)
    print(json_data)
    return HttpResponse(json_data,content_type='application/json')

#another way -student_detail using JsonResponse
def student_detail_JsonResponse(request,pk):
    stu=Student.objects.get(id=pk)
    print(stu)
    serializer=StudentSerializer(stu)#serializing data
   
    return JsonResponse(serializer.data,safe=True)#by default safe=True 


#Queryset-All Student Data
def students(request):
    stu=Student.objects.all()
    print(stu)
    serializer=StudentSerializer(stu,many=True)#serializing data
    print("Serializer ",serializer)
    print("Serializer Data:",serializer.data)
    json_data=JSONRenderer().render(serializer.data)
    print(json_data)
    return HttpResponse(json_data,content_type='application/json')

#another way -student_detail using JsonResponse
def students_JsonResponse(request):
    stu=Student.objects.all()
    print(stu)
    serializer=StudentSerializer(stu,many=True)#serializing data and queryset so set many=True 
    #stu is non_dict set safe=False which is by default safe=True
    return JsonResponse(serializer.data,safe=False)#by default safe=True as queryset 

#Student Create
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def student_create(request):
    if request.method=="POST":
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        serializer=StudentSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'Data created'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json ')
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')
    
#get studentdata through mapp.py
@csrf_exempt
def getstudent(request):
    if request.method=="GET":
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id = pythondata.get('id',None)
        if id is not None:
            stu=Student.objects.get(id=id)
            serializer=StudentSerializer(stu)
            json_data=JSONRenderer().render(serializer.data)#its for response
            return HttpResponse(json_data,content_type='application/json')
        stu=Student.objects.all()
        serializer=StudentSerializer(stu,many=True)
        json_data=JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type='application/json')
    #Add Student Data
    if request.method=="POST":
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        serializer=StudentSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'Student Created'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')
    # Partial Update Student Data
    if request.method=="PUT":
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)#converting to python native
        id=pythondata.get('id')
        stu=Student.objects.get(id=id)
        #partially Updating
        serializer=StudentSerializer(stu,data=pythondata,partial=True)
        
        if serializer.is_valid():
            serializer.save()
            res={'msg':'Data Updated'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')

    # Complete Update Student Data
    if request.method=="PATCH":
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)#converting to python native
        id=pythondata.get('id')
        stu=Student.objects.get(id=id)
        #Complete Updating
        serializer=StudentSerializer(stu,data=pythondata)
        
        if serializer.is_valid():
            serializer.save()
            res={'msg':'Data Updated'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')
    #Deleting Data
    if request.method=="DELETE":
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id=pythondata.get('id',None)
        if id is not None:
            stu=Student.objects.get(id=id)
            
            stu.delete()
            res={'msg':'Data Deleted!!'}
            # json_data=JSONRenderer().render(res)
            # return HttpResponse(json_data,content_type='application/json')
            return JsonResponse(res,safe=False)
        res={'msg':'Unable to  Delete Data Deleted!!'}
        json_data=JSONRenderer().render(res)
        return HttpResponse(json_data,content_type='application/json')

#Rewriting getstudent with Class Based View
@method_decorator(csrf_exempt,name='dispatch')
class StudentGetView(View):
    def get(self,request,*args,**kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id = pythondata.get('id',None)
        if id is not None:
            stu=Student.objects.get(id=id)
            serializer=StudentSerializer(stu)
            json_data=JSONRenderer().render(serializer.data)#its for response
            return HttpResponse(json_data,content_type='application/json')
        stu=Student.objects.all()
        serializer=StudentSerializer(stu,many=True)
        json_data=JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type='application/json')

    def post(self,request,*args,**kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        serializer=StudentSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'Student Created'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')
    
    def put(self,request,*args,**kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)#converting to python native
        id=pythondata.get('id')
        stu=Student.objects.get(id=id)
        #partially Updating
        serializer=StudentSerializer(stu,data=pythondata,partial=True)
        
        if serializer.is_valid():
            serializer.save()
            res={'msg':'Data Updated'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')
    
    def patch(self,request,*args,**kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)#converting to python native
        id=pythondata.get('id')
        stu=Student.objects.get(id=id)
        #Complete Updating
        serializer=StudentSerializer(stu,data=pythondata)
        
        if serializer.is_valid():
            serializer.save()
            res={'msg':'Data Updated'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')
    
    def delete(self,request,*args,**kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id=pythondata.get('id',None)
        if id is not None:
            stu=Student.objects.get(id=id)
            
            stu.delete()
            res={'msg':'Data Deleted!!'}
            # json_data=JSONRenderer().render(res)
            # return HttpResponse(json_data,content_type='application/json')
            return JsonResponse(res,safe=False)
        res={'msg':'Unable to  Delete Data Deleted!!'}
        json_data=JSONRenderer().render(res)
        return HttpResponse(json_data,content_type='application/json')
    
   
