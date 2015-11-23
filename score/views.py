# -*- coding: utf-8 -*-

from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.filters import DjangoFilterBackend, SearchFilter

from score.models import Score, CurrentScore
from score.serializers import ScoreSerializer, CurrentScoreSerializer
from score.filters import ScoreFilter, CurrentScoreFilter


class ScoreView(ReadOnlyModelViewSet):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter,)
    search_fields = ('user__username', 'game',)
    filter_class = ScoreFilter


class CurrentScoreView(ReadOnlyModelViewSet):
    queryset = CurrentScore.objects.all()
    serializer_class = CurrentScoreSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = CurrentScoreFilter
