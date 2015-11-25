# -*- coding: utf-8 -*-

from django.conf.urls import url, patterns, include
from rest_framework.routers import DefaultRouter
from users.views import UserView, ProfileView

router = DefaultRouter()
router.register(r'users', UserView)
router.register(r'profiles', ProfileView)

urlpatterns = patterns(
    '',
    url(r'^', include(router.urls)),
)
