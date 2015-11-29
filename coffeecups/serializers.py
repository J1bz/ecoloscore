# -*- coding: utf-8 -*-

from rest_framework.serializers import ModelSerializer
from coffeecups.models import Take, Throw, CupPolicy


class TakeSerializer(ModelSerializer):
    class Meta:
        model = Take
        fields = ('id', 'user', 'date',)


class ThrowSerializer(ModelSerializer):
    class Meta:
        model = Throw
        fields = ('id', 'user', 'date',)


class CupPolicySerializer(ModelSerializer):
    class Meta:
        model = CupPolicy
        read_only_fields = ('users',)
        fields = (
            'id',
            'name',
            'comment',
            'users',
            'no_takes',
            'take_of_the_day',
            'take_malus',
            'throw',
        )
