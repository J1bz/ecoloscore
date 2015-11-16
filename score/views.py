# -*- coding: utf-8 -*-

from rest_framework.viewsets import ReadOnlyModelViewSet

from score.models import Score, CurrentScore
from score.serializers import ScoreSerializer, CurrentScoreSerializer


class ScoreView(ReadOnlyModelViewSet):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer


class CurrentScoreView(ReadOnlyModelViewSet):
    queryset = CurrentScore.objects.all()
    serializer_class = CurrentScoreSerializer
