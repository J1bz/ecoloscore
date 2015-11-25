# -*- coding: utf-8 -*-

from django_filters import FilterSet, CharFilter, NumberFilter
from django.contrib.auth.models import User
from users.models import Profile


class UserFilter(FilterSet):
    username = CharFilter(name='username', lookup_type='icontains',
                          label='username icontains filter')
    email = CharFilter(name='email', lookup_type='icontains',
                       label='email icontains filter')
    first_name = CharFilter(name='first_name', lookup_type='icontains',
                            label='first_name icontains filter')
    last_name = CharFilter(name='last_name', lookup_type='icontains',
                           label='last_name icontains filter')

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'is_staff',
        )


class ProfileFilter(FilterSet):
    user = NumberFilter(name='user', label='filter by user id')
    rfid_tag = CharFilter(name='rfid_tag', label='rfid_tag contains filter')
    rfid_tag_sub = CharFilter(name='rfid_tag', lookup_type='icontains',
                              label='rfid_tag icontains filter')
    favorite_song = CharFilter(name='favorite_song', lookup_type='icontains',
                               label='favorite_song icontains filter')

    class Meta:
        model = Profile
        fields = (
            'user',
            'rfid_tag',
            'rfid_tag_sub',
            'favorite_song',
        )
