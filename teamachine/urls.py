__author__ = 'luan'

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^(?P<user_id>[0-9]+)/$', views.home, name='home'),
    url(r'^(?P<user_id>[0-9]+)/create/$', views.create, name='create'),
    url(r'^(?P<user_id>[0-9]+)/tearegister/$', views.tearegister, name='tearegister'),
    url(r'^(?P<user_id>[0-9]+)/execute/$', views.execute, name='execute'),
    url(r'^(?P<user_id>[0-9]+)/order/$', views.order, name='order'),
    url(r'^(?P<user_id>[0-9]+)/manage/$', views.manage, name='manage'),
    url(r'^(?P<user_id>[0-9]+)/help/$', views.help, name='help'),
    url(r'^singup/$', views.singup, name='signup'),
    url(r'^register/$', views.register, name='register'),
]