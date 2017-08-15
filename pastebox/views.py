from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

import datetime
from random import randint

from .models import Post

def index(request):
	# Delete any existing posts if they are past expiry
	for p in Post.objects.all():
		if p.date and p.date <= datetime.date.today():
			p.delete()

	# Divide posts into pages of 10 
	post_list = Post.objects.all()
	page = request.GET.get('page', 1)

	paginator = Paginator(post_list, 10)
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)

	#Field for setting minimum constraint on date of expiry.
	date_tomorrow = datetime.date.today() + datetime.timedelta(days=1)
	date_tomorrow = date_tomorrow.isoformat()

	context = {'date_tomorrow' : date_tomorrow, 'posts' : posts}
	
	return render(request, 'pastebox/index.html', context)

def detail(request, post_url):
	post = Post.objects.get(url=post_url)
	post.views += 1
	# post = get_object_or_404(Post, pk=post_url)
	return render(request, 'pastebox/detail.html', {'post': post})


def save(request):
	#Generate unique URL for new post
	while True:
		
		customURL = ""		
		for i in range(0,6):
			customURL += str(randint(0,9))
		# existingURL = Post.objects.get(customURL)
		
		# if not existingURL:
		break

	p = Post(
		name = request.POST['name'], 
		content = request.POST['content'], 
		url = customURL
	)	


	if (request.POST['date']):
		p.date = request.POST['date']
	p.save()	
	# return render(request, 'pastebox/detail.html', {
	# 	'post': p,
	# })
	return HttpResponseRedirect(reverse('pastebox:detail', args=(p.url,)))	

def delete(request, post_url):
	post = Post.objects.get(url=post_url)
	post.delete()
	return HttpResponseRedirect(reverse('pastebox:index'))

def search(request):
	search_term = request.GET['searchbox']

	search_results = Post.objects.filter(
		Q(name__icontains=search_term) | 
		Q(content__icontains=search_term) 
	)
	print(search_results)

	context = { 'search_term' : search_term, 'search_results' : search_results}
	return render(request, 'pastebox/search.html', context)