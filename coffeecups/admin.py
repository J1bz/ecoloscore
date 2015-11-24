# -*- coding: utf-8 -*-

from django.contrib import admin
from coffeecups.models import (
    Take, TakeForm, Throw, ThrowForm, CupPolicy, CupPolicyForm)


class TakeAdmin(admin.ModelAdmin):
    model = TakeForm
    list_display = ('user', 'date',)
    search_fields = ('user__username',)


class ThrowAdmin(admin.ModelAdmin):
    model = ThrowForm
    list_display = ('user', 'date',)
    search_fields = ('user__username',)


class CupPolicyAdmin(admin.ModelAdmin):
    model = CupPolicyForm
    list_display = (
        'name',
        'comment',
        'no_takes',
        'take_of_the_day',
        'take_malus',
        'throw',
    )
    search_fields = (
        'name',
        'comment',
        'users__username',
        'take_of_the_day',
        'take_malus',
        'throw',
    )

admin.site.register(Take, TakeAdmin)
admin.site.register(Throw, ThrowAdmin)
admin.site.register(CupPolicy, CupPolicyAdmin)
