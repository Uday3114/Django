from django.shortcuts import render

# Create your views here.
def seventh_info(request):
	insert_msg='My Name is BHANU'

	my_info={'insert_msg':insert_msg}

	template_name='seventh.html'

	return render(request,template_name=template_name,context=my_info)
