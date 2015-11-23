# -*- coding: utf-8 -*-

from django_filters import FilterSet, CharFilter, NumberFilter, DateTimeFilter
from coffeecups.models import Take, Throw, CupPolicy


class TakeFilter(FilterSet):
    user = NumberFilter(name='user', label='filter by user id')

    date_on_label = 'filter cups taken on provided date / time'
    date_on = DateTimeFilter(name='date', label=date_on_label)
    date_after_label = 'filter cups taken after or on provided date / time'
    date_after = DateTimeFilter(name='date', lookup_type='gte',
                                label=date_after_label)
    date_before_label = 'filter cups taken before or on provided date / time'
    date_before = DateTimeFilter(name='date', lookup_type='lte',
                                 label=date_before_label)

    class Meta:
        model = Take
        fields = (
            'user',
            'date_on',
            'date_after',
            'date_before',
        )


class ThrowFilter(FilterSet):
    user = NumberFilter(name='user', label='filter by user id')

    date_on_label = 'filter cups thrown on provided date / time'
    date_on = DateTimeFilter(name='date', label=date_on_label)
    date_after_label = 'filter cups thrown after or on provided date / time'
    date_after = DateTimeFilter(name='date', lookup_type='gte',
                                label=date_after_label)
    date_before_label = 'filter cups thrown before or on provided date / time'
    date_before = DateTimeFilter(name='date', lookup_type='lte',
                                 label=date_before_label)

    class Meta:
        model = Throw
        fields = (
            'user',
            'date_on',
            'date_after',
            'date_before',
        )


class CupPolicyFilter(FilterSet):
    name = CharFilter(name='name', lookup_type='icontains',
                      label='name icontains filter')
    comment = CharFilter(name='comment', lookup_type='icontains',
                         label='comment icontains filter')
    user = NumberFilter(name='users', label='filter by user id in users')
    take = NumberFilter(name='take__value',
                        label='filter if value is in take values')
    throw = NumberFilter(name='throw__value',
                         label='filter if value is in throw values')

    class Meta:
        model = CupPolicy
        fields = (
            'name',
            'comment',
            'user',
            'take',
            'throw',
        )
