from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser, AbstractUser)
from django.core.mail import send_mail
from django.db import models
from django.utils.translation import ugettext_lazy as _

from project_name.apps.core.manager import UserManager
from project_name.apps.core.models import (
    Group, Role, Types
)
from project_name.apps.core.utils.fields import (
    BaseModel, BaseUUIDModel, BaseAuthUUIDModel
)

AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


class CustomUser(AbstractBaseUser):
    email = models.EmailField(
        _('email address'),
        max_length=255,
        unique=True,
    )
    firstName = models.CharField(
        _('first name'), max_length=40, blank=True, null=True, unique=False)
    lastName = models.CharField(
        _('last name'), max_length=40, blank=True, null=True, unique=False)
    displayName = models.CharField(
        _('display name'), max_length=14, blank=True, null=True, unique=False)
    isActive = models.BooleanField(_('is_active'), default=True)
    isAdmin = models.BooleanField(_('is_admin '), default=False)
    groupId = models.ForeignKey(
        Group, verbose_name=_('group'),
        related_name="%(app_label)s_%(class)s_groupId",
        on_delete=models.SET_NULL, blank=True, null=True)
    roleId = models.ForeignKey(
        Role, verbose_name=_('role'),
        related_name="%(app_label)s_%(class)s_roleId",
        on_delete=models.SET_NULL, blank=True, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def get_full_name(self):
        full_name = '{0:s} {1:s}'.format(self.firstName, self.lastName)
        return full_name.strip()

    def get_short_name(self):
        return self.firstName

    @property
    def name(self):
        if self.firstName:
            return self.firstName
        elif self.displayName:
            return self.displayName
        return 'You'

    def guess_display_name(self):
        if self.displayName:
            return
        if self.firstName and self.lastName:
            dn = "%s %s" % (self.first_name, self.lastName[0])
        elif self.firstName:
            dn = self.firstName
        else:
            dn = 'You'
        self.displayName = dn.strip()

    def email_user(self, subject, message, from_email=None):
        send_mail(subject, message, from_email, [self.email])

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def get_profile(self):
        profile = UserProfile.objects.select_related('userId').get(pk=self)
        return profile

    @property
    def is_active(self):
        return self.isActive

    @property
    def is_staff(self):
        return self.isAdmin

    def __str__(self):
        return self.email

    class Meta:
        abstract = True


class User(CustomUser):
    class Meta(CustomUser.Meta):
        swappable = AUTH_USER_MODEL
        verbose_name = _('01. user')
        verbose_name_plural = _('01. users')
        db_table = 'user'






