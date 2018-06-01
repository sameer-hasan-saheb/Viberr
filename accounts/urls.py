from django.conf.urls import url
from .import views
import django.contrib.auth.views

app_name = 'accounts'

urlpatterns = [
    url(r'^register/$',views.UserFormView.as_view(), name='register'),
    url(r'^login/$', views.UserLogin.as_view(), name='login'),
    url(r'^logout/$', django.contrib.auth.views.logout, { 'next_page' : 'accounts:login' }, name='logout'),
    #url(r'^login/$',auth_views.login,name='login'),
    #url(r'^logout/$',auth_views.logout, { 'next_page' : 'music:login' },name='logout'),

    #url(r'^login/$', django.contrib.auth.views.login, name='login'),
    #url(r'^logout/$',django.contrib.auth.views.logout,name='logout'),
]
