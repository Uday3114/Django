from django.shortcuts import render

# Create your views here.
def third_info(request):
	insert_msg='HERO'

	my_info={'insert_msg':insert_msg}

	template_name='third.html'

	return render(request,template_name=template_name,context=my_info)
