# -*- coding: utf-8 -*-

from django.db.models import (Model, ForeignKey, CharField, TextField,
                              DateTimeField, IntegerField)
from django.forms import ModelForm, CharField as formCharField, Textarea

from django.contrib.auth.models import User
from score.models import Score


class Point(Model):
    name = CharField(max_length=32)
    comment = TextField(blank=True)
    bonus = IntegerField()

    def __unicode__(self):
        return self.name


class PointForm(ModelForm):
    comment = formCharField(required=False, widget=Textarea)

    class Meta:
        model = Point
        fields = ('name', 'comment',)


class Check(Model):
    user = ForeignKey(User)
    point = ForeignKey(Point)
    date = DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        Score(user=self.user, value=self.point.bonus, game='c').save()

        super(Check, self).save(*args, **kwargs)

    def __unicode__(self):
        return '{} checked {} at {}'.format(self.user, self.point, self.date)


class CheckForm(ModelForm):
    class Meta:
        model = Check
        fields = ('user', 'point',)
