# -*- coding: utf-8 -*-

from rest_framework.serializers import ModelSerializer

from users.models import Profile


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'user', 'rfid_tag', 'favorite_song',)
