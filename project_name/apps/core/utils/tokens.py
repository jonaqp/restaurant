from datetime import date
from django.conf import settings
from django.utils.http import int_to_base36, base36_to_int
from django.utils.crypto import constant_time_compare, salted_hmac
from django.utils import six


class TokenGenerator(object):
    def make_token(self, user):
        return self._make_token_with_timestamp(user, self._num_days(self._today()))

    def check_token(self, user, token):
        try:
            ts_b36, _hash = token.split("-")
        except ValueError:
            return False

        try:
            ts = base36_to_int(ts_b36)
        except ValueError:
            return False

        if not constant_time_compare(self._make_token_with_timestamp(user, ts), token):
            return False

        if (self._num_days(self._today()) - ts) > getattr(settings, 'TOKEN_TIMEOUT_DAYS', 7):
            return False

        return True

    def _make_token_with_timestamp(self, user, timestamp):
        ts_b36 = int_to_base36(timestamp)

        key_salt = "TokenGenerator"
        value = (six.text_type(user.pk) + six.text_type(user.dateCreated) + six.text_type(timestamp))
        _hash = salted_hmac(key_salt, value).hexdigest()[::2]
        return "%s-%s" % (ts_b36, _hash)

    def _num_days(self, dt):
        return (dt - date(2001, 1, 1)).days

    def _today(self):
        return date.today()


token_generator = TokenGenerator()
