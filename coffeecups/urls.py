# -*- coding: utf-8 -*-

from django.conf.urls import url, patterns, include
from rest_framework.routers import DefaultRouter
from coffeecups.views import TakeView, ThrowView, CupPolicyView

router = DefaultRouter()
router.register(r'takes', TakeView)
router.register(r'throws', ThrowView)
router.register(r'policies', CupPolicyView)

urlpatterns = patterns(
    '',
    url(r'^', include(router.urls)),
)
