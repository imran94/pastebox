import datetime

from django.db import models
from django.utils import timezone

class Post(models.Model):
	name = models.CharField(max_length=200)
	content = models.TextField()
	date = models.DateField(default=None, blank=True, null=True)
	url = models.CharField(max_length=8, default=None, blank=True, null=True, unique=True)
	views = models.IntegerField(default=0)

	def __str__(self):
		return self.name

class Analytics(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	device = models.CharField(max_length=50)
	os = models.CharField(max_length=50)
	browser = models.CharField(max_length=50)
	ip_address = models.CharField(max_length=50)
	pub_date = models.DateTimeField(default=timezone.now)