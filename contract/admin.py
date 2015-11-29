# -*- coding: utf-8 -*-

from django.contrib import admin
from contract.models import (
    ContractPolicy, ContractPolicyForm,
    ValueGreaterContract, ValueLowerContract, ValueContractForm,
    BoundedValueContract, BoundedValueContractForm,
    )

from score.models import Score


def evaluate(modeladmin, request, queryset):
    queryset.update(evaluated=False)
    for contract in queryset.all():
        if contract.observation is not None:
            evaluation = contract.check_obs()
            if evaluation not in ['ok', 'partial', 'ko']:
                # something went wrong
                break

            else:
                if evaluation == 'ok':
                    score = contract.policy.respected_bonus

                elif evaluation == 'partial':
                    score = contract.policy.partial_bonus

                else:
                    score = contract.policy.unrespected_malus

                concerned_users = []
                for user in contract.u_subjects.all():
                    concerned_users.append(user)

                for group in contract.g_subjects.all():
                    for user in group.user_set.all():
                        if user not in concerned_users:
                            concerned_users.append(user)

                for user in concerned_users:
                    Score(user=user, value=score, game='t').save()

            contract.evaluated = True
            contract.save()


class ContractPolicyAdmin(admin.ModelAdmin):
    form = ContractPolicyForm
    list_display = (
        'id',
        'name',
        'comment',
        'respected_bonus',
        'partial_bonus',
        'unrespected_malus',
    )
    search_fields = (
        'name',
        'comment',
        'respected_bonus',
        'partial_bonus',
        'unrespected_malus',
    )
    actions = [evaluate]


class ValueContractAdmin(admin.ModelAdmin):
    form = ValueContractForm
    list_display = (
        'subjects_list',
        'value',
        'partial',
        'start_period',
        'end_period',
        'observation',
        'evaluated',
    )
    search_fields = (
        'comment',
        'policy__name',
    )
    actions = [evaluate]

    def subjects_list(self, contract):
        subjects = ''

        users = contract.u_subjects.all()
        groups = contract.g_subjects.all()

        for user in users:
            subjects += 'user: {}, '.format(user.username)

        for group in groups:
            subjects += 'group: {}, '.format(group.name)

        return subjects.strip()


class BoundedValueContractAdmin(admin.ModelAdmin):
    form = BoundedValueContractForm
    list_display = (
        'subjects_list',
        'upper_bound',
        'lower_bound',
        'start_period',
        'end_period',
        'observation',
        'evaluated',
    )
    search_fields = (
        'comment',
        'policy__name',
    )
    actions = [evaluate]

    def subjects_list(self, contract):
        subjects = ''

        users = contract.u_subjects.all()
        groups = contract.g_subjects.all()

        for user in users:
            subjects += 'user: {}, '.format(user.username)

        for group in groups:
            subjects += 'group: {}, '.format(group.name)

        return subjects.strip()


admin.site.register(ContractPolicy, ContractPolicyAdmin)
admin.site.register(ValueGreaterContract, ValueContractAdmin)
admin.site.register(ValueLowerContract, ValueContractAdmin)
admin.site.register(BoundedValueContract, BoundedValueContractAdmin)
