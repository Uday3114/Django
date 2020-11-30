from django.shortcuts import render

# Create your views here.
def second_info(request):
	insert_msg='My Name is UDAY'

	my_info={'insert_msg':insert_msg}

	template_name='second.html'

	return render(request,template_name=template_name,context=my_info)
