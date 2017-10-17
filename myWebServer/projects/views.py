# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import Project

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
