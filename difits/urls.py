"""difits URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
import polls.views
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^register/', polls.views.register, name='register'),
    url(r'^$', login, {'template_name':'login.html'}, name='login'),
    url(r'^$', polls.views.registrationSuccess, name='registrationSuccess'),
    url(r'^progress/', polls.views.progress, name='progress'),
#    url(r'^skill/', polls.views.skill_list, name='skill_list'),
    url(r'^details/', polls.views.detail, name='detail'),
#    url(r'^student/(?P<student>[0-9]+)$', polls.views.mainGUI, name='mainGUI'),
    url(r'^logout/', polls.views.logout_view,name='logout'),
    url(r'^info_form/(?P<userid>[0-9]+)$', polls.views.post_new, name='registration'),
    url(r'^retrieve_password_form/$', polls.views.retrieve_password_form, name='retrieve_password_form'),
    url(r'^retrieve/$', polls.views.retrieve, name='retrieve'),
    url(r'^exercise/(?P<skillid>[0-9]+)$', polls.views.exercise, name='exercise'),
    url(r'^mastery/(?P<skillid>[0-9]+)$', polls.views.mastery, name='mastery'),
    url(r'^tutorial/(?P<skillid>[0-9]+)$', polls.views.tutorial, name='tutorial'),
    url(r'^checkworkingstep', polls.views.checkworkingstep, name='checkworkingstep'),
    url(r'^getworkingstephint', polls.views.getworkingstephint, name='getworkingstephint'),
    url(r'^getworkingstepanswer', polls.views.getworkingstepanswer, name='getworkingstepanswer'),
    url(r'^mas_checkworkingstep', polls.views.mas_checkworkingstep, name='mas_checkworkingstep'),
    url(r'^mas_get_questions', polls.views.mas_get_questions, name='mas_get_questions'),
    url(r'^get_masworkingstepanswer', polls.views.get_masworkingstepanswer, name='get_masworkingstepanswer'),
    url(r'^get_masworkingstephint', polls.views.get_masworkingstephint, name='get_masworkingstephint'),
    url(r'^get_tutorial', polls.views.get_tutorial, name='get_tutorial'),
    url(r'^update_tutorial_progress', polls.views.update_tutorial_progress, name='update_tutorial_progress'),

]
