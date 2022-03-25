

from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from api import serializers
from modelserializor.models import Student_Table
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
import io
from rest_framework.parsers import JSONParser
#Fro Class Base View
from django.utils.decorators import method_decorator
from django.views import  View
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


#Student Create
from django.views.decorators.csrf import csrf_exempt

    
#get studentdata through mapp.py
@csrf_exempt
def getstudent(request):
    if request.method=="GET":
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id = pythondata.get('id',None)
        if id is not None:
            stu=Student_Table.objects.get(id=id)
            serializer=StudentSerializer(stu)
            json_data=JSONRenderer().render(serializer.data)#its for response
            return HttpResponse(json_data,content_type='application/json')
        stu=Student_Table.objects.all()
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
        stu=Student_Table.objects.get(id=id)
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
        stu=Student_Table.objects.get(id=id)
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
            stu=Student_Table.objects.get(id=id)
            
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
            stu=Student_Table.objects.get(id=id)
            serializer=StudentSerializer(stu)
            json_data=JSONRenderer().render(serializer.data)#its for response
            return HttpResponse(json_data,content_type='application/json')
        stu=Student_Table.objects.all()
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
        stu=Student_Table.objects.get(id=id)
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
        stu=Student_Table.objects.get(id=id)
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
            stu=Student_Table.objects.get(id=id)
            
            stu.delete()
            res={'msg':'Data Deleted!!'}
            # json_data=JSONRenderer().render(res)
            # return HttpResponse(json_data,content_type='application/json')
            return JsonResponse(res,safe=False)
        res={'msg':'Unable to  Delete Data Deleted!!'}
        json_data=JSONRenderer().render(res)
        return HttpResponse(json_data,content_type='application/json')

#function based api_view
from rest_framework.decorators import api_view
from rest_framework.response import Response
'''
#GET Request
@api_view()#by default GET here like @api_view(['GET',])
def hello_world(request):
    return Response({'msg':'Hello Word'})'''

#POST Request
@api_view(['GET','POST'])  
def hello_world(request):
    if request.method == "GET":
        return Response({'msg':'This is GET request'})
   

    if request.method == "POST":
        print(request.data)
        return Response({'msg':'This is post request','data':request.data})

#Perform crud using api_view 

@api_view(['GET','POST','PUT','DELETE'])
def student_api_view(request):
    if request.method == "GET":
        id=request.data.get('id')
        if id is not None:
            stu=Student_Table.objects.get(pk=id)
            serializer=StudentSerializer(stu)
            return Response(serializer.data)
        stu=Student_Table.objects.all()
        serializer=StudentSerializer(stu,many=True)
        return Response(serializer.data)
    if request.method =="POST":
        print('Parsed Data:',request.data)
        parse_data=request.data
        serializer=StudentSerializer(data=parse_data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    if request.method =="PUT":
        print('Parsed Data:',request.data)
        parsed_data=request.data
        id=parsed_data.get('id')
        if id is not None:
            stu=Student_Table.objects.get(pk=id)
            serializer=StudentSerializer(stu,data=parsed_data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'Data Updated'},status=status.HTTP_201_CREATED)
            return Response(serializer.errors)
    
    if request.method =="DELETE":
        print('Parsed Data:',request.data)
        parsed_data=request.data
        id=parsed_data.get('id')
        stu=Student_Table.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Data Deleted'})

#Passing pk explicitly in function
@api_view(['GET','POST','PUT','PATCH','DELETE'])
#PATCH-partial update
#PUT-complete update
def student_api_view_pk(request,pk=None):#passing pk = None
    if request.method == "GET":
        # id=request.data.get('id')
        id=pk#as pk is in function so we can do like this also
        if id is not None:
            stu=Student_Table.objects.get(pk=id)
            serializer=StudentSerializer(stu)
            return Response(serializer.data,status=status.HTTP_200_OK)
        stu=Student_Table.objects.all()
        serializer=StudentSerializer(stu,many=True)
        return Response(serializer.data)
    if request.method =="POST":
        print('Parsed Data:',request.data)
        parse_data=request.data
        serializer=StudentSerializer(data=parse_data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

    
    if request.method =="PATCH":
        print('Parsed Data:',request.data)
        parsed_data=request.data
        # id=parsed_data.get('id')
        id=pk
        if id is not None:
            stu=Student_Table.objects.get(pk=id)
            serializer=StudentSerializer(stu,data=parsed_data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'Data Updated'})
            return Response(serializer.errors)

    if request.method =="PUT":
        print('Parsed Data:',request.data)
        parsed_data=request.data
        # id=parsed_data.get('id')
        id=pk
        if id is not None:
            stu=Student_Table.objects.get(pk=id)
            serializer=StudentSerializer(stu,data=parsed_data)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'Data Updated'},status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        return Response({'status':'id not found'},status=status.HTTP_400_BAD_REQUEST)
    
    if request.method =="DELETE":
        print('Parsed Data:',request.data)
        parsed_data=request.data
        # id=parsed_data.get('id')
        id=pk
        stu=Student_Table.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Data Deleted'})
   
#Using Class Based APIView
from rest_framework.views import APIView
class StudentClassBasedAPI(APIView):
    def get(self,request,format=None):
        stu=Student_Table.objects.all()
        serializer=StudentSerializer(stu,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
   
