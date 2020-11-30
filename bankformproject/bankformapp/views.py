from django.shortcuts import render
from .forms import AccRegistration
from django.http import httpResponse

# Create your views here.
def accregisterview(request):
	form=AccRegistration()
	if request.method=='POST':
		form=AccRegistration(request.POST)
		if form.is_valid():
			form.save()
			print('Data got inserted into Database successfully')
			return success(request)
	return render(request,'bankformapp/display.html',{'form':form})

def success(request):
	s1="<center><h1>Acc Details Uploaded Successfully</h1></center>"
	return HttpResponse(s1)
