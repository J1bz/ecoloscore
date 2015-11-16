# -*- coding: utf-8 -*-

from django.conf.urls import url, patterns, include
from rest_framework.routers import DefaultRouter
from checkpoints.views import PointView, CheckView

router = DefaultRouter()
router.register(r'points', PointView)
router.register(r'checks', CheckView)

urlpatterns = patterns(
    '',
    url(r'^', include(router.urls)),
)
