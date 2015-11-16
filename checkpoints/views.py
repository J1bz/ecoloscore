# -*- coding: utf-8 -*-

from rest_framework.viewsets import ReadOnlyModelViewSet

from checkpoints.models import Point, Check
from checkpoints.serializers import PointSerializer, CheckSerializer


class PointView(ReadOnlyModelViewSet):
    queryset = Point.objects.all()
    serializer_class = PointSerializer


class CheckView(ReadOnlyModelViewSet):
    queryset = Check.objects.all()
    serializer_class = CheckSerializer
