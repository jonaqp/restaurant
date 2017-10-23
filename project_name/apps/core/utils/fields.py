import uuid

from django.conf import settings
from django.db import models
from django.db.models import ForeignKey
from django.utils.translation import ugettext_lazy as _

from project_name.apps.core.middleware.current_user import UserMiddleware
from project_name.apps.core.utils.funct_dates import str_datetime
from ..constants import SELECT_DEFAULT_TUPLE, STATUS_MODEL, ENABLED
from ..queryset import AuditableManager

AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


class CurrentUserField(ForeignKey):
    def __init__(self, to_field=None, to=AUTH_USER_MODEL, **kwargs):
        self.add_only = kwargs.pop('add_only', False)
        kwargs.update({
            'editable': False,
            'null': True,
            'to': to,
            'to_field': to_field,
        })
        super().__init__(**kwargs)

    def pre_save(self, model_instance, add):
        if add or not self.add_only:
            user = UserMiddleware.get_user()
            if user:
                setattr(model_instance, self.attname, user.pk)
                return user.pk
        return super().pre_save(model_instance, add)


class TimeStampedModel(models.Model):
    dateCreated = models.DateTimeField(
        blank=True, null=True, editable=False, auto_now_add=True,
        verbose_name=_('date created'))
    dateModified = models.DateTimeField(
        blank=True, null=True, editable=False, auto_now=True,
        verbose_name=_('date modified'))

    class Meta:
        abstract = True


class CreatorTimeStampedModel(models.Model):
    createdBy = CurrentUserField(
        add_only=True, verbose_name=_('created by'),
        related_name="%(app_label)s_%(class)s_created_by", )
    modifiedBy = CurrentUserField(
        verbose_name=_('modified by'),
        related_name="%(app_label)s_%(class)s_modified_by")

    class Meta:
        abstract = True


class AuthWithoutTimeStampedModel(TimeStampedModel):
    class Meta:
        abstract = True


class AuthWithTimeStampedModel(TimeStampedModel, CreatorTimeStampedModel):
    class Meta:
        abstract = True


class UUIDModel(models.Model):
    uid = models.UUIDField(editable=False, default=uuid.uuid4)

    class Meta:
        abstract = True


class StatusModel(models.Model):
    isDeleted = models.BooleanField(default=False, editable=False)

    class Meta:
        abstract = True


class StatusCurrent(models.Model):
    currentStatus = models.CharField(
        max_length=10, choices=SELECT_DEFAULT_TUPLE + STATUS_MODEL, default=ENABLED)

    class Meta:
        abstract = True


class ManagerBase(models.Model):
    current = AuditableManager()
    objects = models.Manager()

    def save(self, delete=False, force_delete=False, *args, **kwargs):
        if self.pk:
            self.dateModified = str_datetime()
        else:
            self.dateCreated = str_datetime()
            kwargs['force_insert'] = False
        if delete:
            self.isDeleted = True
        if force_delete:
            return super().delete(*args, **kwargs)
        return super().save(*args, **kwargs)

    def delete(self, force_delete=False, *args, **kwargs):
        self.save(delete=True)
        if force_delete:
            self.save(force_delete=True)
        return super().save(*args, **kwargs)

    class Meta:
        abstract = True


# Model without Creator Stamped Model
class BaseModel(ManagerBase, AuthWithoutTimeStampedModel, StatusModel):
    class Meta:
        abstract = True


class BaseUUIDModel(ManagerBase, UUIDModel, AuthWithoutTimeStampedModel, StatusModel):
    class Meta:
        abstract = True


# Model with Creator Stamped Model
class BaseAuthModel(ManagerBase, AuthWithTimeStampedModel, StatusModel):
    class Meta:
        abstract = True


class BaseAuthUUIDModel(ManagerBase, UUIDModel, AuthWithTimeStampedModel, StatusModel):
    class Meta:
        abstract = True
