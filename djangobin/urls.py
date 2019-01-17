from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	#url(r'^time/$', views.today_is, name='time'),
	url(r'^user/(?P<username>[A-Za-z0-9]+)/$', views.profile, name='profile'),
	#url(r'^books/$', views.book_category, name='book_category'),
	#url(r'^books/(?P<category>[\w-]+)/$', views.book_category,name='book_category'),
	#url(r'^extra/$', views.extra_args, {'arg1': 1, 'arg2': (10, 20, 30)}, name='extra_args'),
	url(r'^trending/$', views.trending_snippets, name='trending_snippets'),
	url(r'^trending/(?P<language_slug>[\w]+)/$', views.trending_snippets, name='trending_snippets'),
	url(r'^(?P<snippet_slug>[\d]+)/$', views.snippet_detail, name='snippet_detail'),
	url(r'^tag/(?P<tag>[\w-]+)/$', views.tag_list, name='tag_list'),
]