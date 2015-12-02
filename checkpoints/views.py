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
    queryset = Check.objects.all()
    serializer_class = CheckSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter,)
    search_fields = ('user__username', 'point__name',)
    filter_class = CheckFilter
