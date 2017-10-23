from django.db import models
from django.utils.translation import ugettext_lazy as _

from project_name.apps.core import constants as core_constants
from project_name.apps.core.models import Role, Permission
from project_name.apps.core.utils.fields import BaseModel


class Module(BaseModel):
    band_choice = core_constants.TYPE_BAND_OPTIONS
    name = models.CharField(
        _('name'), max_length=200, null=True, blank=True)
    icon = models.CharField(
        _('icon'), max_length=200, null=True, blank=True)
    match = models.CharField(
        _('match'), default="#", max_length=200, null=False, blank=False)
    urlName = models.CharField(
        _('urlName'), max_length=200, null=True, blank=True)
    reference = models.CharField(
        _('reference'), unique=True, max_length=100, null=False, blank=False)
    order = models.IntegerField(
        _('order'), default=0, null=False, blank=False)
    bandType = models.CharField(
        _('band type'), choices=band_choice,
        max_length=80, default=core_constants.CODE_BAND_ONE)

    class Meta:
        ordering = ['order']
        unique_together = ['name']
        verbose_name = _('01. module')
        verbose_name_plural = _('01. modules')

    def __str__(self):
        return self.name


class ModuleItem(BaseModel):
    name = models.CharField(
        _('name'), max_length=200, null=True, blank=True)
    icon = models.CharField(
        _('icon'), max_length=200, null=True, blank=True)
    match = models.CharField(
        _('match'), default="#", max_length=200, null=False, blank=False)
    urlName = models.CharField(
        _('urlName'), max_length=200, null=True, blank=True)
    reference = models.CharField(
        _('reference'), unique=True, max_length=100, null=False, blank=False)
    order = models.IntegerField(
        _('order'), null=False, blank=False, default=0)
    moduleId = models.ForeignKey(
        Module, verbose_name=_('module'),
        related_name="%(app_label)s_%(class)s_moduleId",
    )

    def module_text(self):
        return "{0}".format(self.moduleId)

    class Meta:
        ordering = ['moduleId']
        verbose_name = _('02. module item')
        verbose_name_plural = _("02. module items")

    def __str__(self):
        return "{0}-{1}".format(self.moduleId, self.name)


class RoleModule(BaseModel):
    roleId = models.ForeignKey(
        Role, verbose_name=_('role'),
        related_name="%(app_label)s_%(class)s_roleId",
        on_delete=models.SET_NULL, blank=True, null=True)
    moduleId = models.ForeignKey(
        Module, verbose_name=_('module'),
        related_name="%(app_label)s_%(class)s_moduleId",
        on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        unique_together = ["roleId", "moduleId"]
        verbose_name = _('03. module team')
        verbose_name_plural = _('03. module teams')

    def get_moduleitem_list(self):
        module_item = RoleModuleItem.objects.filter(roleModuleId=self)
        return ", ".join([p.moduleItemId.name for p in module_item])

    def get_module_order(self):
        return self.moduleId.order

    def __str__(self):
        return "{0}".format(self.moduleId)


class RoleModuleItem(BaseModel):
    roleModuleId = models.ForeignKey(
        RoleModule, verbose_name=_('role module'),
        related_name="%(app_label)s_%(class)s_roleModuleId",
    )
    moduleItemId = models.ForeignKey(
        ModuleItem, verbose_name=_('module item'),
        related_name="%(app_label)s_%(class)s_moduleItemId",
    )

    class Meta:
        unique_together = ['roleModuleId', 'moduleItemId']
        verbose_name = _('04. module item team')
        verbose_name_plural = _('04. module item teams')

    def __str__(self):
        return "{0} | {1}".format(self.roleModuleId, self.moduleItemId.name)
