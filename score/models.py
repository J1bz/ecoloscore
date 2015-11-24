# -*- coding: utf-8 -*-

from django.core.exceptions import ObjectDoesNotExist
from django.db.models import (Model, ForeignKey, CharField, IntegerField,
                              DateTimeField, OneToOneField)
from django.forms import ModelForm

from django.contrib.auth.models import User


class Score(Model):
    GAMES = (
        ('p', 'checkpoints'),
        ('c', 'coffeecups'),
    )

    user = ForeignKey(User)
    game = CharField(max_length=1, choices=GAMES)
    value = IntegerField()
    date = DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.pk:
            old_score = Score.objects.get(pk=self.pk)
            try:
                old_user_current_score = CurrentScore.objects.get(
                    user=old_score.user)
                old_user_current_score.update(-old_score.value)

            except ObjectDoesNotExist:
                old_user_current_score = CurrentScore.objects.create(
                    user=old_score.user, value=-old_score.value)
                old_user_current_score.save()

        try:
            user_current_score = CurrentScore.objects.get(user=self.user)
            user_current_score.update(self.value)

        except ObjectDoesNotExist:
            user_current_score = CurrentScore.objects.create(
                user=self.user, value=self.value)
            user_current_score.save()

        super(Score, self).save(*args, **kwargs)

    def __unicode__(self):
        return '{} scored {} ({})'.format(self.user, self.value, self.game)


class ScoreForm(ModelForm):
    class Meta:
        model = Score
        fields = ('user', 'game', 'value',)


class CurrentScore(Model):
    user = OneToOneField(User)
    value = IntegerField()

    def update(self, value):
        self.value += value
        self.save()

    def __unicode__(self):
        return '{} has {} points'.format(self.user, self.value)


class CurrentScoreForm(ModelForm):
    class Meta:
        model = CurrentScore
        fields = ('user', 'value',)
