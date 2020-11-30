from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def insert_operation(request):
	my_data='<marquee style="color:red;font-size:45px">Welcome to kotak bamk thank you for adding account</marquee>'
	return  HttpResponse(my_data)

def update_operation(request):
	my_data='<marquee style="color:red;font-size:45px">Welcome to kotak bamk thank you for updating amount</marquee>'
	return  HttpResponse(my_data)

def withdraw_operation(request):
	my_data='<marquee style="color:red;font-size:45px">Please collect your cash & your available balance : 10000</marquee>'
	return  HttpResponse(my_data)