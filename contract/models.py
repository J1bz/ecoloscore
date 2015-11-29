# -*- coding: utf-8 -*-

from django.db.models import (
    Model, ManyToManyField, CharField, DateTimeField, ForeignKey,
    IntegerField, TextField, BooleanField)
from django.forms import ModelForm, CharField as formCharField, Textarea

from django.contrib.auth.models import User, Group


class ContractPolicy(Model):
    name = CharField(max_length=32)
    comment = TextField(blank=True)

    respected_bonus = IntegerField()
    partial_bonus = IntegerField()
    unrespected_malus = IntegerField()

    def __unicode__(self):
        return 'Contract policy: {}'.format(self.name)


class ContractPolicyForm(ModelForm):
    comment = formCharField(required=False, widget=Textarea)

    class Meta:
        model = ContractPolicy
        fields = (
            'name',
            'comment',
            'respected_bonus',
            'partial_bonus',
            'unrespected_malus',
        )


class AbstractContract(Model):
    u_subjects = ManyToManyField(User, blank=True)
    g_subjects = ManyToManyField(Group, blank=True)
    comment = TextField(blank=True)

    policy = ForeignKey(ContractPolicy)

    start_period = DateTimeField()
    end_period = DateTimeField()
    record_date = DateTimeField(auto_now_add=True)

    observation = IntegerField(blank=True, null=True)
    observation_date = DateTimeField(blank=True, null=True)

    evaluated = BooleanField(default=False)

    class Meta:
        abstract = True


class ValueGreaterContract(AbstractContract):
    value = IntegerField()
    partial = IntegerField()

    def check_obs(self):
        if self.observation > self.value:
            return 'ok'

        elif self.observation > self.partial:
            return 'partial'

        else:
            return 'ko'


class ValueLowerContract(AbstractContract):
    value = IntegerField()
    partial = IntegerField()

    def check_obs(self):
        if self.observation < self.value:
            return 'ok'

        elif self.observation < self.partial:
            return 'partial'

        else:
            return 'ko'


class ValueContractForm(ModelForm):
    class Meta:
        model = ValueLowerContract
        fields = (
            'u_subjects',
            'g_subjects',
            'comment',
            'value',
            'partial',
            'policy',
            'start_period',
            'end_period',
            'observation',
            'observation_date',
        )


class BoundedValueContract(AbstractContract):
    upper_bound = IntegerField()
    lower_bound = IntegerField()
    partial_upper_bound = IntegerField()
    partial_lower_bound = IntegerField()

    def check_obs(self):
        obs = self.observation

        if self.upper_bound > obs and obs > self.lower_bound:
            return 'ok'

        elif (self.partial_upper_bound > obs and
              obs > self.partial_lower_bound):
            return 'partial'

        else:
            return 'ko'


class BoundedValueContractForm(ModelForm):
    class Meta:
        model = BoundedValueContract
        fields = (
            'u_subjects',
            'g_subjects',
            'comment',
            'upper_bound',
            'lower_bound',
            'partial_upper_bound',
            'partial_lower_bound',
            'policy',
            'start_period',
            'end_period',
            'observation',
            'observation_date',
        )
