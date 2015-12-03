# -*- coding: utf-8 -*-

from datetime import datetime, timedelta

from django.core.exceptions import ObjectDoesNotExist
from django.db.models import (Model, ForeignKey, DateTimeField, CharField,
                              ManyToManyField, IntegerField, TextField)
from django.forms import ModelForm, CharField as formCharField, Textarea

from django.contrib.auth.models import User
from score.models import Score

# TODO: make sure that a user can't be in 2 cup policies


class Take(Model):
    """
    A take is a record for a user taking a cup at a given date at a cup
    distributor (we don't record where).
    """

    user = ForeignKey(User)
    date = DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        """
        Depending on the number of taken cups during the last 12 hours,
        the player's score is updated with a bonus or a malus referenced in
        the administrable cup policy attached to the user.

        If a user did not take any cup during a day, a crontab is supposed to
        update his score with a bonus referenced in the same user attached
        cup policy.
        """

        if not self.pk:  # only if take does not already exist
            try:
                policy = CupPolicy.objects.get(users=self.user)

                now = datetime.now()
                day = timedelta(hours=12)

                # Cups taken in the last working day
                taken_cups = Take.objects.filter(date__gte=(now - day),
                                                 user=self.user)
                taken_cups_number = len(taken_cups)

                if taken_cups_number == 0:  # it means this take is the first
                    points = policy.take_of_the_day

                else:
                    points = policy.take_malus

                s = Score.objects.create(user=self.user, game='c',
                                         value=points)
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
    """
    A throw is a record for a user throwing a cup at a given date in a cup
    bin (we don't record where).
    """

    user = ForeignKey(User)
    date = DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        """
        If the number of thrown cups is inferior to the number of taken cups
        during the last 12 hours, the player's score is updated with a bonus
        referenced in the administrable cup policy attached to the user.

        If it is superior, well, it is a good thing to throw other's people
        cups, but since we don't want users to abuse of the system we just
        don't record it.
        """

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
                                             value=points)
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


class CupPolicy(Model):
    """
    A cup policy is a configurable object allowing ecoloscore administrators
    to change some score bonuses/maluses and to choose which users are
    concerned by this policy.
    """

    name = CharField(max_length=32)
    comment = TextField(blank=True)
    users = ManyToManyField(User, blank=True)

    # points given at the end of the day if you didn't take any cup during a
    # week day (should be handled by a crontab)
    no_takes = IntegerField()

    # points given if the cup is the first one a user took this day
    take_of_the_day = IntegerField()

    # points given (should be negative) a cup has already been taken this day
    take_malus = IntegerField()

    # points given if you throwed a cup you took earlier this day
    throw = IntegerField()

    def __unicode__(self):
        return 'Cup policy: {}'.format(self.name)

    class Meta:
        verbose_name_plural = 'cup policies'


class CupPolicyForm(ModelForm):
    comment = formCharField(required=False, widget=Textarea)

    class Meta:
        model = CupPolicy
        fields = (
            'name',
            'comment',
            'users',
            'no_takes',
            'take_of_the_day',
            'take_malus',
            'throw',
        )
