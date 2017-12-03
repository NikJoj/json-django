from django.http import HttpResponse
import json
from . models import *
from django.http import StreamingHttpResponse
from django.views.decorators.csrf import csrf_exempt
from appone.models import data
from django.http import JsonResponse
from collections import namedtuple
from django.core import serializers

def index(request):
	return HttpResponse("<h1>appone homepage")

@csrf_exempt
def ind(request):
	if request.method=='POST':
		received_json_data=json.loads(request.body)
		#print ((received_json_data))
		x = namedtuple("object1", received_json_data.keys())(*received_json_data.values())
		data2=data.objects.create()
		data2.fname=x.fname
		data2.lname=x.lname
		data2.passo=x.passo
		data2.stud=x.stud
		data2.insti=x.insti
		data2.phone=x.phone
		data2.email=x.email
		data2.save()
		return StreamingHttpResponse(str(received_json_data))
	return StreamingHttpResponse('was GET')

def req(request):
	if request.method=='GET':
		#data1=noti.objects.all()
		data2 = serializers.serialize('json', noti.objects.all())
		
		#for x in data1:
		#	data3=x
		#x=dict(x)
		return HttpResponse(data2, content_type="application/json")
