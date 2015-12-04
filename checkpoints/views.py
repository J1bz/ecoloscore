# -*- coding: utf-8 -*-

from rest_framework.authentication import (
    TokenAuthentication, SessionAuthentication)
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import (
    authentication_classes, permission_classes)
from rest_framework.viewsets import GenericViewSet, ReadOnlyModelViewSet
from rest_framework.mixins import (
    ListModelMixin, RetrieveModelMixin, CreateModelMixin)
from rest_framework.filters import DjangoFilterBackend, SearchFilter

from common.permissions import IsAdminOrAuthentReadOnly
from checkpoints.models import Point, Check
from checkpoints.serializers import PointSerializer, CheckSerializer
from checkpoints.filters import PointFilter, CheckFilter


@authentication_classes((TokenAuthentication, SessionAuthentication,))
@permission_classes((IsAuthenticated,))
class PointView(ReadOnlyModelViewSet):
    """
    Each point is a record for an arduino station graunting you score points
    for tagging it with your RFID device.
    """

    queryset = Point.objects.all()
    serializer_class = PointSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter,)
    search_fields = ('name', 'comment', 'bonus',)
    filter_class = PointFilter


@authentication_classes((TokenAuthentication, SessionAuthentication,))
@permission_classes((IsAdminOrAuthentReadOnly,))
class CheckView(GenericViewSet,
                ListModelMixin,
                RetrieveModelMixin,
                CreateModelMixin):
    """
    A check is an association of a player being at a given point at a given
    time.

    A Check creation triggers record of a Score entry for the deserved amount
    of points and for game `p` (checkPoints).

    Two consecutive checks cannot be recorded for the same user at the
    same point if there is not at least a 30 seconds time difference.
    It prevents users from cheating/checking twice. This should NOT be
    tested here. It should be done by a raspberry or an arduino station.
    But since we run out of time...
    """

    queryset = Check.objects.all()
    serializer_class = CheckSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter,)
    search_fields = ('user__username', 'point__name',)
    filter_class = CheckFilter
