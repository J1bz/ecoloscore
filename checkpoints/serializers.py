# -*- coding: utf-8 -*-

from rest_framework.serializers import ModelSerializer
from checkpoints.models import Point, Check


class PointSerializer(ModelSerializer):
    class Meta:
        model = Point
        fields = ('id', 'name', 'comment',)


class CheckSerializer(ModelSerializer):
    class Meta:
        model = Check
        fields = ('id', 'user', 'point', 'date',)
