# -*- coding: utf-8 -*-

"""ecoloscore URL Configuration

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
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^ecoauth/', include('ecoauth.urls')),
    url(r'^users/', include('users.urls')),
    url(r'^checkpoints/', include('checkpoints.urls')),
    url(r'^coffeecups/', include('coffeecups.urls')),
    url(r'^score/', include('score.urls')),

    url(r'^docs/', include('rest_framework_swagger.urls')),
]

# webmin
urlpatterns += staticfiles_urlpatterns()

# serving media files
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
