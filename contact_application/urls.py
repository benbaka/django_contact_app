"""contact_application URL Configuration

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
from contacts.views import contact_views
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^contacts/$', contact_views.index),
    url(r'^contacts/new$', contact_views.new),
    url(r'^contacts/(?P<id>\d+)/edit$', contact_views.edit),
    url(r'^contacts/(?P<id>\d+)/update$', contact_views.edit),
    url(r'^contacts/(?P<id>\d+)/show$', contact_views.show),
    url(r'^contacts/(?P<id>\d+)/delete$', contact_views.delete),
    url(r'^me$', contact_views.me),

]
