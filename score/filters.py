# -*- coding: utf-8 -*-

from django_filters import FilterSet, CharFilter, NumberFilter, DateTimeFilter
from score.models import Score, CurrentScore


class ScoreFilter(FilterSet):
    user = NumberFilter(name='user', label='filter by user id')
    game = CharFilter(name='game', label='filter by game shortname')

    value = NumberFilter(name='value',
                         label='scores equal to value')
    value_gt = NumberFilter(name='value', lookup_type='gt',
                            label='scores greater than value')
    value_lt = NumberFilter(name='value', lookup_type='lt',
                            label='scores lower than value')
    value_gte = NumberFilter(name='value', lookup_type='gte',
                             label='scores greater than value or equal')
    value_lte = NumberFilter(name='value', lookup_type='lte',
                             label='scores lower than value or equal')

    date_on_lbl = 'filter values scored on provided date / time'
    date_on = DateTimeFilter(name='date', label=date_on_lbl)
    date_after_lbl = 'filter values scored after or on provided date / time'
    date_after = DateTimeFilter(name='date', lookup_type='gte',
                                label=date_after_lbl)
    date_before_lbl = 'filter values scored before or on provided date / time'
    date_before = DateTimeFilter(name='date', lookup_type='lte',
                                 label=date_before_lbl)

    class Meta:
        model = Score
        fields = (
            'user',
            'game',
            'value',
            'value_gt',
            'value_lt',
            'value_gte',
            'value_lte',
            'date_on',
            'date_after',
            'date_before',
        )


class CurrentScoreFilter(FilterSet):
    user = NumberFilter(name='user', label='filter by user id')
    value = NumberFilter(name='value',
                         label='scores equal to value')
    value_gt = NumberFilter(name='value', lookup_type='gt',
                            label='scores greater than value')
    value_lt = NumberFilter(name='value', lookup_type='lt',
                            label='scores lower than value')
    value_gte = NumberFilter(name='value', lookup_type='gte',
                             label='scores greater than value or equal')
    value_lte = NumberFilter(name='value', lookup_type='lte',
                             label='scores lower than value or equal')

    class Meta:
        model = CurrentScore
        fields = (
            'user',
            'value',
            'value_gt',
            'value_lt',
            'value_gte',
            'value_lte',
        )
