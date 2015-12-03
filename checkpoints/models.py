# -*- coding: utf-8 -*-

from django.db.models import (Model, ForeignKey, CharField, TextField,
                              DateTimeField, IntegerField)
from django.forms import ModelForm, CharField as formCharField, Textarea

from django.contrib.auth.models import User
from score.models import Score


class Point(Model):
    """
    Each point is a record for an arduino station graunting you score points
    for tagging it with your RFID device.
    """

    # Administration identifier
    name = CharField(max_length=32)
    comment = TextField(blank=True)

    # Arduino identifier used to know where a user is
    arduino = CharField(max_length=64)

    # Each point has its own bonus value. If a point requires efforts
    # to reach, it should grant many points.
    bonus = IntegerField()

    def __unicode__(self):
        return self.name


class PointForm(ModelForm):
    comment = formCharField(required=False, widget=Textarea)

    class Meta:
        model = Point
        fields = ('name', 'comment', 'arduino', 'bonus',)


class Check(Model):
    """
    A check is an association of a player being at a given point at a given
    time.
    """

    user = ForeignKey(User)
    point = ForeignKey(Point)
    date = DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        """
        A Check creation triggers record of a Score entry for the deserved
        amount of points and for game `p` (checkPoints).
        """

        Score(user=self.user, value=self.point.bonus, game='p').save()

        super(Check, self).save(*args, **kwargs)

    def __unicode__(self):
        return '{} checked {} at {}'.format(self.user, self.point, self.date)


class CheckForm(ModelForm):
    class Meta:
        model = Check
        fields = ('user', 'point',)
