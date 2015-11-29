# -*- coding: utf-8 -*-

from datetime import datetime, timedelta

from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand

from django.contrib.auth.models import User
from coffeecups.models import Take, CupPolicy
from score.models import Score


class Command(BaseCommand):
    help = """Command that should be triggered each working day to grant
    points to users who did not take any cup during the last day"""

    def handle(self, *args, **options):
        for user in User.objects.all():
            # Users can be management entities. To be sure that a user should
            # be considered as a player, we try to access his profile data
            # (where his/her rfid tag is saved) and if it does not exist we
            # just skip this user
            try:
                user.profile

            except ObjectDoesNotExist:
                break

            now = datetime.now()
            more_than_day = timedelta(hours=16)
            period = now - more_than_day

            user_takes = Take.objects.filter(user=user, date__gte=period)

            if not user_takes.exists():
                try:
                    policy = CupPolicy.objects.get(users=user)

                except ObjectDoesNotExist:
                    # If a user does not have a policy... well... he should
                    # not be very active in ecoloscore games so we just ignore
                    # him
                    break

                points = policy.no_takes
                Score.objects.create(user=user, game='c', value=points).save()
