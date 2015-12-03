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
    """
    A take is a record for a user taking a cup at a given date at a cup
    distributor (we don't record where).

    Depending on the number of taken cups during the last 12 hours,
    the player's score is updated with a bonus or a malus referenced in
    the administrable cup policy attached to the user.

    If a user did not take any cup during a day, a crontab is supposed to
    update his score with a bonus referenced in the same user attached
    cup policy.
    """

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
    """
    A throw is a record for a user throwing a cup at a given date in a cup
    bin (we don't record where).

    If the number of thrown cups is inferior to the number of taken cups
    during the last 12 hours, the player's score is updated with a bonus
    referenced in the administrable cup policy attached to the user.

    If it is superior, well, it is a good thing to throw other's people
    cups, but since we don't want users to abuse of the system we just
    don't record it.
    """

    queryset = Throw.objects.all()
    serializer_class = ThrowSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = ThrowFilter


@authentication_classes((TokenAuthentication, SessionAuthentication,))
@permission_classes((IsAuthenticated,))
class CupPolicyView(ReadOnlyModelViewSet):
    """
    A cup policy is a configurable object allowing ecoloscore administrators
    to change some score bonuses/maluses and to choose which users are
    concerned by this policy.
    """

    queryset = CupPolicy.objects.all()
    serializer_class = CupPolicySerializer
    filter_backends = (DjangoFilterBackend, SearchFilter,)
    search_fields = ('name', 'comment',)
    filter_class = CupPolicyFilter
