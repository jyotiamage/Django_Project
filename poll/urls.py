from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

app_name = 'poll'
'''url(r'^$', views.index, name = 'index'),
	url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),'''
urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^login/$', views.login_view, name='login'),
	url(r'^logout/$', views.logout_view, name='logout'),
	url(r'^accounts/login/$', auth_views.login, name='acclogin'),
	url(r'^signup/$', views.signup_view, name='signup'),
	url(r'^index/', views.index, name='index'),
    url(r'^polls/$', views.index, name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='result'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),

]