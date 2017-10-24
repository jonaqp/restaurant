from debug_toolbar.settings import PANELS_DEFAULTS

from .settings import *

env_file = str(PROJECT_ROOT.path('security/environ_local.env'))
environ.Env.read_env(str(env_file))

DEBUG = env.bool('DEBUG')

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '[::1]', '*']
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

SECRET_KEY = SECRET_FILE

# Database
DATABASES = {
    'default': env.db("SQLITE_URL"),
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'entropydb',
#         'USER': 'jonathan',
#         'PASSWORD': 'jonathan',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }


CACHES = {
    'default': env.cache()
}

DJANGO_APPS = (

)
THIRD_PARTY_APPS = (
    'debug_toolbar',
    'django_extensions',
)
LOCAL_APPS = (

)
INSTALLED_APPS += DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

PANELS_DEFAULTS += (
    'ddt_request_history.panels.request_history.RequestHistoryPanel',
)
CONFIG_DEFAULTS = {
    'RESULTS_CACHE_SIZE': 3,
    'SHOW_COLLAPSED': True
}
INTERNAL_IPS = ['localhost', '127.0.0.1', '[::1]']
DEBUG_TOOLBAR_CONFIG = {
    'JQUERY_URL': '/static/themes/global/core/libraries/jquery.min.js',
    'SHOW_TOOLBAR_CALLBACK': 'ddt_request_history.panels.request_history.allow_ajax',
    'INTERCEPT_REDIRECTS': False,
}
DEBUG_TOOLBAR_PATCH_SETTINGS = True

# https://www.google.com/settings/security/lesssecureapps
EMAIL_BACKEND = env('DJANGO_EMAIL_BACKEND')
EMAIL_CONFIG = env.email_url('EMAIL_URL')
vars().update(EMAIL_CONFIG)

ADMIN_URL = env('ADMIN_URL')

SESSION_COOKIE_SECURE = False
SESSION_COOKIE_HTTPONLY = False
CSRF_COOKIE_SECURE = False

AWS_STATIC_LOCATION = 'static'
AWS_PUBLIC_MEDIA_LOCATION = 'media/public'
AWS_PRIVATE_MEDIA_LOCATION = 'media/private'

LOGGING['loggers'].update({
    'project_name': {
        'handlers': ['console'],
        'level': 'DEBUG',
        'propagate': True,
    },
    'django': {
        'handlers': ['console'],
        'level': 'DEBUG',
        'propagate': True,
    },
    'django.db.backends': {
        'handlers': ['django'],
        'level': 'DEBUG',
        'propagate': False,
    },
    'performance': {
        'handlers': ['console'],
        'level': 'INFO',
        'propagate': True,
    },
})
