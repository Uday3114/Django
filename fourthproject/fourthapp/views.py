from django.shortcuts import render
import datetime

# Create your views here.
def greeting_info(request):

	my_time=datetime.datetime.now()
	fmt='%H'
	my_hours=int(my_time.strftime(fmt))
	insert_msg='Wishing you all very_'

	if my_hours<12:
		insert_msg+="GoodMorning!!!"

	elif my_hours<16:
		insert_msg+="GoodAfternoon!!!"

	elif my_hours<20:
		insert_msg+="GoodEvening!!!"

	else:
		insert_msg+="GoodNight!!!"

	my_info={'my_time':my_time,'insert_msg':insert_msg}


	template_name='fourthapp/html/greeting.html'

	return render(request,template_name=template_name,context=my_info)