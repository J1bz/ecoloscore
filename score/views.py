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
    """
    A Score entry is a discrete differential value at a given date for a user
    refering to a game.

    A score entry also updates the user's current score.

    Instead of recording a single score value for each user, it allows
    flexibility to display score tables that can be filtered for a particular
    game and/or between two dates.

    For example, we can imagine a monthly event where people could see
    everyone else's scores before setting the time period for the next month.
    """

    queryset = Score.objects.all()
    serializer_class = ScoreSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter,)
    search_fields = ('user__username', 'game',)
    filter_class = ScoreFilter


@authentication_classes((TokenAuthentication, SessionAuthentication,))
@permission_classes((IsAuthenticated,))
class CurrentScoreView(ReadOnlyModelViewSet):
    """
    Current scores are a single value per user recording all score deltas
    since the beggining of the game.

    It can be used to simulates levels for people to reach, and give them
    rewards in function of their value since the beggining for instance.
    """

    queryset = CurrentScore.objects.all()
    serializer_class = CurrentScoreSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = CurrentScoreFilter
