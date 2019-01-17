from django.shortcuts import HttpResponse, render, render_to_response
import datetime
from django import template
from django.conf import settings

def index(request):
	return HttpResponse("<p>Hello Django</p>")

def snippet_detail(request, snippet_slug):
	return HttpResponse('viewing snippet #{}'.format(snippet_slug))

def trending_snippets(request, language_slug=''):
	return HttpResponse('trending {} snippets'.format(language_slug if language_slug else ''))

def tag_list(request, tag):
	return HttpResponse("viewing tag #{}".format(tag))

def today_is(request):
	now = datetime.datetime.now()
	#t = template.Template("<html><body>Current date and time: {{now}} </body></html>")
	
	t = template.loader.get_template('djangobin/datetime.html')
	#c = template.Context({'now': now})
	#html = "<html><body>Current date and time: {0} </body></html>".format(now)
	#html = t.render(c)
	#html = t.render({'now' : now})
	#return HttpResponse(html)
	#return render_to_response('djangobin/datetime.html', {'now':now})
	return render(request, 'djangobin/datetime.html', {
		'now':now, 
		'template_name': 'djangobin/nav.html',
		'base_dir' : settings.BASE_DIR
		})


def profile(request, username):
	return HttpResponse("<p>Profile page of #{}</p>".format(username))


def book_category(request, category='sci-fi'):
	return HttpResponse("<p>Books in {} category</p>".format(category))


def extra_args(request, arg1=None, arg2=None):
	return HttpResponse("<p>arg1: {} <br> arg2: {} </p>".format(arg1, arg2))