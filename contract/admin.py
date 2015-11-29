# -*- coding: utf-8 -*-

from django.contrib import admin
from contract.models import (
    ContractPolicy, ContractPolicyForm,
    ValueGreaterContract, ValueLowerContract, ValueContractForm,
    BoundedValueContract, BoundedValueContractForm,
    )


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
