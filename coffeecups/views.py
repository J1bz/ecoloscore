# -*- coding: utf-8 -*-

from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.filters import DjangoFilterBackend, SearchFilter

from coffeecups.models import Take, Throw, Points, CupPolicy
from coffeecups.serializers import (TakeSerializer, ThrowSerializer,
                                    PointsSerializer, CupPolicySerializer)
from coffeecups.filters import TakeFilter, ThrowFilter, CupPolicyFilter


class TakeView(ReadOnlyModelViewSet):
    queryset = Take.objects.all()
    serializer_class = TakeSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = TakeFilter


class ThrowView(ReadOnlyModelViewSet):
    queryset = Throw.objects.all()
    serializer_class = ThrowSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = ThrowFilter


class PointsView(ReadOnlyModelViewSet):
    queryset = Points.objects.all()
    serializer_class = PointsSerializer


class CupPolicyView(ReadOnlyModelViewSet):
    queryset = CupPolicy.objects.all()
    serializer_class = CupPolicySerializer
    filter_backends = (DjangoFilterBackend, SearchFilter,)
    search_fields = ('name', 'comment',)
    filter_class = CupPolicyFilter
