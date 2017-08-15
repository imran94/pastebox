from django.contrib import admin

# Register your models here.
from .models import Post, Analytics

admin.site.register(Post)
admin.site.register(Analytics)