# -*- coding: utf-8 -*-

from django_filters import FilterSet, CharFilter, NumberFilter, DateTimeFilter
from checkpoints.models import Point, Check


class PointFilter(FilterSet):
    name = CharFilter(name='name', lookup_type='icontains',
                      label='name icontains filter')
    comment = CharFilter(name='comment', lookup_type='icontains',
                         label='comment icontains filter')
    bonus = NumberFilter(name='bonus',
                         label='filter points where bonus is equal to value')

    class Meta:
        model = Point
        fields = (
            'name',
            'comment',
            'bonus',
        )


class CheckFilter(FilterSet):
    user = NumberFilter(name='user', label='filter by user id')
    point = NumberFilter(name='point', label='filter by point id')

    date_on_lbl = 'filter points checked on provided date / time'
    date_on = DateTimeFilter(name='date', label=date_on_lbl)
    date_after_lbl = 'filter points checked after or on provided date / time'
    date_after = DateTimeFilter(name='date', lookup_type='gte',
                                label=date_after_lbl)
    date_before_lbl = 'filter points checked before or on provided date / time'
    date_before = DateTimeFilter(name='date', lookup_type='lte',
                                 label=date_before_lbl)

    class Meta:
        model = Check
        fields = (
            'user',
            'point',
            'date_on',
            'date_after',
            'date_before',
        )
