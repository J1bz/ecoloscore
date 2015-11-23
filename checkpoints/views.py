# -*- coding: utf-8 -*-

from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.filters import DjangoFilterBackend, SearchFilter

from checkpoints.models import Point, Check
from checkpoints.serializers import PointSerializer, CheckSerializer
from checkpoints.filters import PointFilter, CheckFilter


class PointView(ReadOnlyModelViewSet):
    queryset = Point.objects.all()
    serializer_class = PointSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter,)
    search_fields = ('name', 'comment', 'bonus',)
    filter_class = PointFilter


class CheckView(ReadOnlyModelViewSet):
    queryset = Check.objects.all()
    serializer_class = CheckSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter,)
    search_fields = ('user__username', 'point__name',)
    filter_class = CheckFilter
