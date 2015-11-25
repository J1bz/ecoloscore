# -*- coding: utf-8 -*-

from django.db.models import Model, OneToOneField, CharField
from django.forms import ModelForm

from django.contrib.auth.models import User


class Profile(Model):
    user = OneToOneField(User)
    rfid_tag = CharField(max_length=64)
    favorite_song = CharField(max_length=64)

    def __unicode__(self):
        return '{}\'s profile'.format(self.user)


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('user', 'rfid_tag', 'favorite_song',)
