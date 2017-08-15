import datetime

from django.db import models

class Post(models.Model):
	name = models.CharField(max_length=200)
	content = models.TextField()
	date = models.DateField(default=None, blank=True, null=True)
	url = models.CharField(max_length=5, default=None, blank=True, null=True)
	views = models.IntegerField(default=0)

	def __str__(self):
		return self.name