# -*- coding: utf-8 -*-

from django.db.models import Model, OneToOneField, CharField, FileField
from django.forms import ModelForm

from django.contrib.auth.models import User


class Profile(Model):
    user = OneToOneField(User)
    rfid_tag = CharField(max_length=64)
    favorite_song = FileField(upload_to='songs', blank=True)

    def __unicode__(self):
        return '{}\'s profile'.format(self.user)


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('user', 'rfid_tag', 'favorite_song',)
