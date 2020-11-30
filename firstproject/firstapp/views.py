from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def respond_to_client(request):
	my_output='<marquee style="color:red;font-size:45px">Welcome to ABC</marquee>'
	return  HttpResponse(my_output)