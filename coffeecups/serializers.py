# -*- coding: utf-8 -*-

from rest_framework.serializers import ModelSerializer
from coffeecups.models import Take, Throw, Points, CupPolicy


class TakeSerializer(ModelSerializer):
    class Meta:
        model = Take
        fields = ('id', 'user', 'date',)


class ThrowSerializer(ModelSerializer):
    class Meta:
        model = Throw
        fields = ('id', 'user', 'date',)


class PointsSerializer(ModelSerializer):
    class Meta:
        model = Points
        fields = ('id', 'value',)


class CupPolicySerializer(ModelSerializer):
    class Meta:
        model = CupPolicy
        read_only_fields = ('users', 'take',)
        fields = ('id', 'name', 'comment', 'users', 'take', 'throw',)
