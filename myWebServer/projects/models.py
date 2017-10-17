# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Project(models.Model):
	project_name = models.CharField(max_length=50)
	short_desc = models.TextField()
	project_url = models.CharField(max_length=100)
	def __str__():
		return self.project_name
		

class Screenshot(models.Model):
	image_url = models.CharField(max_length=100)
	project = models.ForeignKey(Project, on_delete=models.CASCADE)
	def __str__():
		return self.image_url
