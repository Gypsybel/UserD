from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^sign_in$', views.sign_in),
    url(r'^register$', views.register),
    url(r'^admin_edit/(?P<id>\d+)$', views.admin_edit),
    url(r'^show/(?P<id>\d+)$', views.show),
    url(r'^logoff$', views.logoff),
    url(r'^addnew$', views.addnew),
    url(r'^dashboard$', views.dashboard),
    url(r'^create$', views.create),
    url(r'^remove/(?P<id>\d+)$', views.remove),
    url(r'^update/(?P<id>\d+)$', views.update),
    url(r'^update_password/(?P<id>\d+)$', views.update_password),
    url(r'^login$', views.login),
    url(r'^edit/(?P<id>\d+)$', views.edit),
    url(r'^edit_description/(?P<id>\d+)$', views.edit_description),
    url(r'^postm/(?P<id>\d+)/(?P<uid>\d+)$', views.postm),
    url(r'^postc/(?P<uid>\d+)/(?P<mid>\d+)/(?P<id>\d+)$', views.postc),
]