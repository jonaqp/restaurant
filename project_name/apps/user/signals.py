import logging
from random import randint

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')
log = logging.getLogger('project_name_console')


@receiver(post_save, sender=AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        first_name = "{0} {1}".format(str("User"), str(randint(0, 999999)))
        instance.firstName = first_name
        instance.save()


