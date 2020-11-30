from django.shortcuts import render
from .forms import StudentRegistration


# Create your views here.
def studentregistrationview(request):
	form = StudentRegistration()
	return render(request,'formapp/display.html',{'form':form})
