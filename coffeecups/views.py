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
from coffeecups.models import Take, Throw, CupPolicy
from coffeecups.serializers import (
    TakeSerializer, ThrowSerializer, CupPolicySerializer)
from coffeecups.filters import TakeFilter, ThrowFilter, CupPolicyFilter


@authentication_classes((TokenAuthentication, SessionAuthentication,))
@permission_classes((IsAdminOrAuthentReadOnly,))
class TakeView(GenericViewSet,
               ListModelMixin,
               RetrieveModelMixin,
               CreateModelMixin):
    queryset = Take.objects.all()
    serializer_class = TakeSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = TakeFilter


@authentication_classes((TokenAuthentication, SessionAuthentication,))
@permission_classes((IsAdminOrAuthentReadOnly,))
class ThrowView(GenericViewSet,
                ListModelMixin,
                RetrieveModelMixin,
                CreateModelMixin):
    queryset = Throw.objects.all()
    serializer_class = ThrowSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = ThrowFilter


@authentication_classes((TokenAuthentication, SessionAuthentication,))
@permission_classes((IsAuthenticated,))
class CupPolicyView(ReadOnlyModelViewSet):
    queryset = CupPolicy.objects.all()
    serializer_class = CupPolicySerializer
    filter_backends = (DjangoFilterBackend, SearchFilter,)
    search_fields = ('name', 'comment',)
    filter_class = CupPolicyFilter
