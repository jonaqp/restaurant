import datetime

from django.conf import settings
from django.core.mail import EmailMessage
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template, render_to_string
from django.utils.translation import ugettext_lazy as _


class EmailTemplate(object):

    @staticmethod
    def get_send_affiliate_html(affiliate):
        from_email = settings.EMAIL_HOST_USER
        subject = _("codigo autenticacion team {0}".format(str(affiliate.teamId.alias)))
        to = [affiliate.email]

        ctx = {
            'title': _('code token team'),
            'username': affiliate.email,
            'token': affiliate.tokenAssociation,
        }

        body = get_template('themes/mailer/affiliate.html').render(ctx)
        msg = EmailMessage(subject=subject,
                           body=body,
                           from_email=from_email,
                           to=to)
        msg.content_subtype = 'html'
        msg.send()
        return True
