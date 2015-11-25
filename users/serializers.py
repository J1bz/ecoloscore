# -*- coding: utf-8 -*-

from rest_framework.serializers import ModelSerializer

from django.contrib.auth.models import User
from users.models import Profile


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'is_staff',
        )


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'user', 'rfid_tag', 'favorite_song',)
