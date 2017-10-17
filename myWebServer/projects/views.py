# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import Project
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
	project_list = Project.objects.all()
	context = {
		'project_list': project_list,
	}
	return render(request, 'projects/index.html',context)

def detail(request, project_id):
	project_list = Project.objects.all()
	context = {
		'project_list': project_list,
	}
	return render(request, 'projects/index.html',context)

def add(request):
 	return render(request, 'projects/add.html')

def submit(request):
	p = Project(project_name=request.POST['project_name'], short_desc=request.POST['project_short_desc'],project_url=request.POST['project_url'])
	p.save()
	return HttpResponseRedirect(reverse('projects:add'))
	return render(request, 'projects/add.html')
