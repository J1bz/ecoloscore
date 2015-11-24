# -*- coding: utf-8 -*-

from datetime import datetime, timedelta

from django.core.exceptions import ObjectDoesNotExist
from django.db.models import (Model, ForeignKey, DateTimeField, CharField,
                              ManyToManyField, IntegerField, TextField)
from django.forms import ModelForm, CharField as formCharField, Textarea

from django.contrib.auth.models import User
from score.models import Score


class Take(Model):
    user = ForeignKey(User)
    date = DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.pk:  # only if take does not already exist
            try:
                policy = CupPolicy.objects.get(users=self.user)

                now = datetime.now()
                day = timedelta(hours=12)

                # Cups taken in the last working day
                taken_cups = Take.objects.filter(date__gte=(now - day),
                                                 user=self.user)
                taken_cups_number = len(taken_cups)

                policy_cups_bonus = policy.take.all()
                if taken_cups_number < len(policy_cups_bonus):
                    points = policy_cups_bonus[taken_cups_number + 1]

                else:
                    points = policy_cups_bonus.reverse()[0]

                s = Score.objects.create(user=self.user, game='c',
                                         value=points.value)
                s.save()

            except ObjectDoesNotExist:
                pass

        super(Take, self).save(*args, **kwargs)

    def __unicode__(self):
        return '{} took a cup at {}'.format(self.user, self.date)


class TakeForm(ModelForm):
    class Meta:
        model = Take
        fields = ('user',)


class Throw(Model):
    user = ForeignKey(User)
    date = DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.pk:  # If thrown already exist
            super(Throw, self).save(*args, **kwargs)

        else:
            try:
                now = datetime.now()
                day = timedelta(hours=12)

                # Cups taken in the last working day
                taken_cups = Take.objects.filter(date__gte=(now - day),
                                                 user=self.user)
                thrown_cups = Throw.objects.filter(date__gte=(now - day),
                                                   user=self.user)

                if len(taken_cups) > len(thrown_cups):
                    policy = CupPolicy.objects.get(users=self.user)
                    points = policy.throw

                    s = Score.objects.create(user=self.user, game='c',
                                             value=points.value)
                    s.save()

                    # Throw is not saved if it is just a throw that is not
                    # part of the game, that is to say if all user taken
                    # cups have already be thrown.
                    super(Throw, self).save(*args, **kwargs)

            except ObjectDoesNotExist:
                pass

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
