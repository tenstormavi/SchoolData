from django.shortcuts import render, render_to_response, RequestContext

from django.contrib import messages
# Create your views here.
from studentinfo.models import *
from .forms import StudentInfoForm
from django.core.context_processors import csrf
from django.template import RequestContext

def homepage(request):
	return render_to_response('homepage.html')

def home(request):

	form = StudentInfoForm(request.POST or None)

	if form.is_valid():
		save_it = form.save(commit=False)
		save_it.save()
		messages.success(request, 'New Entry Inserted. Thankyou.')


	return render_to_response("info.html", 
		                      locals(), 
		                      context_instance=RequestContext(request))

def searchpage(request):
	return render_to_response('search.html', context_instance=RequestContext(request))

def search(request):
	search = request.POST['search']
	items = StudentInfo.objects.filter(first_name__icontains=search)
	return render_to_response('result.html', {'items':items})
