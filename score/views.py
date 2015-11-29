# -*- coding: utf-8 -*-

from rest_framework.authentication import (
    TokenAuthentication, SessionAuthentication)
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import (
    authentication_classes, permission_classes)
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.filters import DjangoFilterBackend, SearchFilter

from score.models import Score, CurrentScore
from score.serializers import ScoreSerializer, CurrentScoreSerializer
from score.filters import ScoreFilter, CurrentScoreFilter


@authentication_classes((TokenAuthentication, SessionAuthentication,))
@permission_classes((IsAuthenticated,))
class ScoreView(ReadOnlyModelViewSet):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter,)
    search_fields = ('user__username', 'game',)
    filter_class = ScoreFilter


@authentication_classes((TokenAuthentication, SessionAuthentication,))
@permission_classes((IsAuthenticated,))
class CurrentScoreView(ReadOnlyModelViewSet):
    queryset = CurrentScore.objects.all()
    serializer_class = CurrentScoreSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = CurrentScoreFilter
