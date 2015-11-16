# -*- coding: utf-8 -*-

from django.conf.urls import url, patterns, include
from rest_framework.routers import DefaultRouter
from checkpoints.views import CurrentView, CurrentScoreView

router = DefaultRouter()
router.register(r'scores', CurrentView)
router.register(r'currentscores', CurrentScoreView)

urlpatterns = patterns(
    '',
    url(r'^', include(router.urls)),
)
