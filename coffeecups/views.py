# -*- coding: utf-8 -*-

from rest_framework.viewsets import ReadOnlyModelViewSet

from coffeecups.models import Take, Throw, Points, CupPolicy
from coffeecups.serializers import (TakeSerializer, ThrowSerializer,
                                    PointsSerializer, CupPolicySerializer)


class TakeView(ReadOnlyModelViewSet):
    queryset = Take.objects.all()
    serializer_class = TakeSerializer


class ThrowView(ReadOnlyModelViewSet):
    queryset = Throw.objects.all()
    serializer_class = ThrowSerializer


class PointsView(ReadOnlyModelViewSet):
    queryset = Points.objects.all()
    serializer_class = PointsSerializer


class CupPolicyView(ReadOnlyModelViewSet):
    queryset = CupPolicy.objects.all()
    serializer_class = CupPolicySerializer
