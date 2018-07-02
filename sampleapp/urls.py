from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from sampleapp import views

app_name = "sampleapp"

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^login/$', views.login, name='login'),
    url(r'^login_failed/$', views.login_failed, name='login_failed'),
    url(r'^login_submit/$', views.login_submit, name='login_submit'),
    url(r'^select/$', views.select, name='select'),
    url(r'^output/$', views.output, name='output')
]
