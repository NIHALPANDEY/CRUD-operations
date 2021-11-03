from functools import partial
from django.shortcuts import render
import requests
import io
from rest_framework.parsers import JSONParser
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def student_api(request):
    if request.method=="GET":
        json_data=request.body
        print(request.body)
        stream=io.BytesIO(json_data)
        print(stream)
        pythondata=JSONParser().parse(stream)
        print(pythondata)
        id=pythondata.get("id",None)
        print(id)
        if id is not None:
            stu=Student.objects.get(id=id)
            serializer=StudentSerializer(stu)
            json_data=JSONRenderer().render(serializer.data)
            return HttpResponse(json_data)
        stu=Student.objects.all()
        serializer=StudentSerializer(stu,many=True)
        json_data=JSONRenderer().render(serializer.data)
        return HttpResponse(json_data)



    if request.method=="POST":
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        serializer=StudentSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res={"msg":"data created"}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data)
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data)


    if request.method=="PUT":
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id=pythondata.get('id')
        stu=Student.objects.get(id=id)
        serializer=StudentSerializer(stu,data=pythondata,partial=False)
        if serializer.is_valid():
            serializer.save()
            res={"msg":"data UPdated"}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data)
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data)


    if request.method=="DELETE":
        json_data=request.body
        stream=io.BytesIO(json_data)
        print(stream)
        pythondata=JSONParser().parse(stream)
        id=pythondata.get('id')
        stu=Student.objects.get(id=id)
        print(stu)
        stu.delete()
        res={"msg":"data deleted"}
        json_data1=JSONRenderer().render(res)
        return HttpResponse(json_data1)