# -*- coding: utf-8 -*-

from django.db.models import (Model, ForeignKey, DateTimeField, CharField,
                              ManyToManyField, IntegerField, TextField)
from django.forms import ModelForm, CharField as formCharField, Textarea

from django.contrib.auth.models import User


class Take(Model):
    user = ForeignKey(User)
    date = DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return '{} took a cup at {}'.format(self.user, self.date)


class TakeForm(ModelForm):
    class Meta:
        model = Take
        fields = ('user',)


class Throw(Model):
    user = ForeignKey(User)
    date = DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return '{} throwed cup at {}'.format(self.user, self.date)


class ThrowForm(ModelForm):
    class Meta:
        model = Throw
        fields = ('user',)


class Points(Model):
    value = IntegerField()

    def __unicode__(self):
        return 'Cup points: {}'.format(self.value)

    class Meta:
        verbose_name_plural = 'points'


class PointsForm(ModelForm):
    class Meta:
        model = Points
        fields = ('value',)


class CupPolicy(Model):
    name = CharField(max_length=32)
    comment = TextField(blank=True)
    users = ManyToManyField(User, blank=True)
    take = ManyToManyField(Points, related_name='take')
    throw = ForeignKey(Points, related_name='throw')

    def __unicode__(self):
        return 'Cup policy: {}'.format(self.name)

    class Meta:
        verbose_name_plural = 'cup policies'


class CupPolicyForm(ModelForm):
    comment = formCharField(required=False, widget=Textarea)

    class Meta:
        model = CupPolicy
        fields = ('name', 'comment', 'users', 'take', 'throw',)
