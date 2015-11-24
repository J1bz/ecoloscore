# -*- coding: utf-8 -*-

from rest_framework.serializers import (
    ModelSerializer, HyperlinkedModelSerializer, IntegerField)
from coffeecups.models import Take, Throw, CupPolicy

from rest_framework.exceptions import ValidationError
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User


class TakeSerializer(ModelSerializer):
    class Meta:
        model = Take
        fields = ('id', 'user', 'date',)


class ThrowSerializer(ModelSerializer):
    class Meta:
        model = Throw
        fields = ('id', 'user', 'date',)


class UserSerializer(HyperlinkedModelSerializer):
    user = IntegerField()

    def validate(self, attrs):
        user_id = attrs.get('user')
        try:
            user = User.objects.get(id=user_id)
            attrs['user'] = user
            return attrs

        except ObjectDoesNotExist:
            message = 'user id {} not found in database'.format(user_id)
            raise ValidationError(message)


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
