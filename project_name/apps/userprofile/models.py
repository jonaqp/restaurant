from django.conf import settings
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.db import models
from django.utils.encoding import force_text
from django.utils.html import format_html
from django.utils.translation import ugettext_lazy as _

from project_name.apps.core import constants as core_constants
from project_name.apps.core.utils.fields import (
    BaseUUIDModel
)
from project_name.apps.core.utils.upload_folder import upload_user_profile
from project_name.apps.core.utils.storages import PublicMediaStorage

AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


class UserProfile(BaseUUIDModel):
    userId = models.OneToOneField(
        AUTH_USER_MODEL, primary_key=True, verbose_name=_('user'),
        related_name="%(app_label)s_%(class)s_userId")
    address = models.CharField(
        _('address'), max_length=200, blank=True, null=True)
    genderTypeId = models.CharField(
        _('gender'), blank=True, null=True, max_length=10,
        choices=core_constants.TYPE_OPTIONS[core_constants.SIS_GENDER_TYPE][1])
    documentIdentityTypeId = models.CharField(
        _('document identity'), blank=True, null=True, max_length=10,
        choices=core_constants.TYPE_OPTIONS[core_constants.SIS_DOCUMENT_IDENTITY_TYPE][1])
    documentIdentityNumber = models.CharField(
        _('document number'), max_length=50, blank=True, null=True)
    homePhone = models.CharField(
        _('home phone'), max_length=50, blank=True, null=True)
    mobilePhone = models.CharField(
        _('mobile phone'), max_length=50, blank=True, null=True)
    logoProfile = models.ImageField(
        _('logo'), storage=PublicMediaStorage,
        upload_to=upload_user_profile, blank=True, null=True)

    def __str__(self):
        return force_text(self.userId.email)

    def get_full_name(self):
        return "{0} {1}".format(self.userId.firstName, self.userId.lastName)

    @property
    def get_user_email(self):
        return self.userId.email

    def get_logo_profile_url(self):
        if self.logoProfile:
            return self.logoProfile.url
        else:
            return static('themes/img/default/default-user-male.jpg')

    def thumb(self):
        if self.logoProfile:
            return format_html(u'<img src="{0:s}" width=60 height=60 />'
                               .format(self.logoProfile.url))
        else:
            img = static('themes/img/default/default-user-male.jpg')
            return format_html(
                u'<img src="{0:s}" width=60 height=60 />'.format(img))

    thumb.short_description = _('Thumbnail')
    thumb.allow_tags = True

    class Meta:
        verbose_name = _("01. Profile")
        verbose_name_plural = _("01. Profiles")
        db_table = 'userProfile'
