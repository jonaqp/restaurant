from django.db import models
from django.utils.translation import ugettext_lazy as _

from . import constants as core_constants
from .manager import TeamManager, PermissionManager
from .utils.fields import BaseUUIDModel


class Group(BaseUUIDModel):
    name = models.CharField(_('name'), max_length=80, unique=True)

    objects = TeamManager()

    class Meta:
        unique_together = ('name',)
        verbose_name = _('01. group')
        verbose_name_plural = _('01. groups')

    def __str__(self):
        return self.name

    def natural_key(self):
        return self.name


class Role(BaseUUIDModel):
    groupId = models.ForeignKey(
        Group, verbose_name=_("group"),
        related_name="%(app_label)s_%(class)s_groupId",
        on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(_('name'), max_length=80, unique=True)
    codename = models.CharField(_('codename'), max_length=80, unique=True)

    class Meta:
        unique_together = ('groupId', 'name', 'codename',)
        verbose_name = _('02. role')
        verbose_name_plural = _('02. roles')

    def __str__(self):
        if self.groupId:
            return "{0}:{1}".format(str(self.groupId.name), str(self.codename))
        else:
            return "{0}:{1}".format(str("----"), str(self.codename))

    def natural_key(self):
        return self.name


class Permission(BaseUUIDModel):
    name = models.CharField(_('name'), max_length=80, unique=True)
    codename = models.CharField(_('codename'), max_length=80, unique=True)

    objects = PermissionManager()

    class Meta:
        unique_together = ('name',)
        verbose_name = _('03. permission')
        verbose_name_plural = _('03. permissions')

    def __str__(self):
        return self.name

    def natural_key(self):
        return self.name


class Types(BaseUUIDModel):
    type_choice = core_constants.TYPE_OPTIONS
    type = models.CharField(_('type'), max_length=10, choices=type_choice)
    code = models.CharField(_('code'), max_length=20, blank=False, null=False)
    name = models.CharField(_('name'), max_length=100, blank=False, null=False)

    class Meta:
        unique_together = ('type', 'code')
        verbose_name = _('04. Type')
        verbose_name_plural = _('04. Types')

    def __str__(self):
        return self.name
