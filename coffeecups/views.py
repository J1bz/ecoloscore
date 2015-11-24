# -*- coding: utf-8 -*-

from rest_framework.authentication import (
    TokenAuthentication, SessionAuthentication)
from rest_framework.decorators import (
    authentication_classes, permission_classes, detail_route)
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import DjangoFilterBackend, SearchFilter
from rest_framework.response import Response

from common.permissions import IsAdminOrAuthentReadOnly
from coffeecups.models import Take, Throw, CupPolicy
from coffeecups.serializers import (
    TakeSerializer, ThrowSerializer, CupPolicySerializer, UserSerializer)
from coffeecups.filters import TakeFilter, ThrowFilter, CupPolicyFilter


@authentication_classes((TokenAuthentication, SessionAuthentication,))
@permission_classes((IsAdminOrAuthentReadOnly,))
class TakeView(ModelViewSet):
    queryset = Take.objects.all()
    serializer_class = TakeSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = TakeFilter


@authentication_classes((TokenAuthentication, SessionAuthentication,))
@permission_classes((IsAdminOrAuthentReadOnly,))
class ThrowView(ModelViewSet):
    queryset = Throw.objects.all()
    serializer_class = ThrowSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = ThrowFilter


@authentication_classes((TokenAuthentication, SessionAuthentication,))
@permission_classes((IsAdminOrAuthentReadOnly,))
class CupPolicyView(ModelViewSet):
    queryset = CupPolicy.objects.all()
    serializer_class = CupPolicySerializer
    filter_backends = (DjangoFilterBackend, SearchFilter,)
    search_fields = ('name', 'comment',)
    filter_class = CupPolicyFilter

    @detail_route(methods=['POST'])
    def add_user(self, request, *args, **kwargs):
        cup_policy = self.get_object()

        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']

        cup_policy.users.create(user=user)

        message = {'message': '{} added to {}'.format(user, cup_policy)}
        return Response(message)

    @detail_route(methods=['POST'])
    def rm_user(self, request, *args, **kwargs):
        cup_policy = self.get_object()

        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']

        cup_policy.users.filter(user=user).delete()

        message = {'message': '{} removed to {}'.format(user, cup_policy)}
        return Response(message)

    # @detail_route(methods=['POST'])
    # def add_take_bonus(self, request, *args, **kwargs):
    #     cup_policy = self.get_object()

    #     serializer = PointsSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)

    #     value = serializer.validated_data['value']

    #     points = Points.objects.create(value=value)
    #     points.save()
    #     cup_policy.take.create(value=value)

    #     message = {'message': '{} take bonus added to {}'.format(value,
    #                                                              cup_policy)}
    #     return Response(message)

    # @detail_route(methods=['POST'])
    # def rm_take_bonus(self, request, *args, **kwargs):
    #     cup_policy = self.get_object()

    #     serializer = PointsSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)

    #     value = serializer.validated_data['value']

    #     cup_policy.take.filter(value=value).delete()

    #     message = {'message': '{} take bonus removed to {}'.format(value,
    #                                                                cup_policy)}
    #     return Response(message)

    # @detail_route(methods=['POST'])
    # def set_throw_bonus(self, request, *args, **kwargs):
    #     cup_policy = self.get_object()

    #     serializer = PointsSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)

    #     value = serializer.validated_data['value']

    #     points = Points.objects.create(value=value)
    #     points.save()
    #     cup_policy.throw = points
    #     cup_policy.save()

    #     message = {'message': '{} throw bonus set to {}'.format(cup_policy,
    #                                                             value)}
    #     return Response(message)
