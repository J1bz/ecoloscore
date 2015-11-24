# -*- coding: utf-8 -*-

from rest_framework.authentication import (
    TokenAuthentication, SessionAuthentication)
from rest_framework.decorators import (
    authentication_classes, permission_classes)
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.filters import DjangoFilterBackend, SearchFilter

from common.permissions import IsAdminOrAuthentReadOnly
from coffeecups.models import Take, Throw, Points, CupPolicy
from coffeecups.serializers import (TakeSerializer, ThrowSerializer,
                                    PointsSerializer, CupPolicySerializer)
from coffeecups.filters import TakeFilter, ThrowFilter, CupPolicyFilter


@authentication_classes((TokenAuthentication, SessionAuthentication,))
@permission_classes((IsAdminOrAuthentReadOnly,))
class TakeView(ReadOnlyModelViewSet):
    queryset = Take.objects.all()
    serializer_class = TakeSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = TakeFilter


@authentication_classes((TokenAuthentication, SessionAuthentication,))
@permission_classes((IsAdminOrAuthentReadOnly,))
class ThrowView(ReadOnlyModelViewSet):
    queryset = Throw.objects.all()
    serializer_class = ThrowSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = ThrowFilter


@authentication_classes((TokenAuthentication, SessionAuthentication,))
@permission_classes((IsAdminOrAuthentReadOnly,))
class PointsView(ReadOnlyModelViewSet):
    queryset = Points.objects.all()
    serializer_class = PointsSerializer


@authentication_classes((TokenAuthentication, SessionAuthentication,))
@permission_classes((IsAdminOrAuthentReadOnly,))
class CupPolicyView(ReadOnlyModelViewSet):
    queryset = CupPolicy.objects.all()
    serializer_class = CupPolicySerializer
    filter_backends = (DjangoFilterBackend, SearchFilter,)
    search_fields = ('name', 'comment',)
    filter_class = CupPolicyFilter
