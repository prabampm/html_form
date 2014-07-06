from django.http import HttpResponse
from webapp.models import *
from django.shortcuts import render,render_to_response
def home(request):
	if request.POST:
		firstname=request.POST.get('firstname')
		lastname= request.POST.get('lastname')
		email = request.POST.get('email')
		a= Contact(
          first_name=firstname,
          last_name=lastname,
          email=email
			)
		a.save()
	b=Contact.objects.all()
	return render(request,'index.html',locals())


# Create your views here.
