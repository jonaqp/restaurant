"""
Django settings for dj_gen project.
"""
import os

import environ
from django.utils.translation import ugettext_lazy as _

PROJECT_ROOT = environ.Path(__file__) - 3
APPS_DIR = PROJECT_ROOT.path('apps/')
env = environ.Env()

DEBUG = True

ALLOWED_HOSTS = []

# Application definition
DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

THIRD_PARTY_APPS = (
    'rest_framework',
    'rest_framework.authtoken',
    'rest_auth',
    'corsheaders',
    'allauth',
    'allauth.account',

)


CORS_ORIGIN_ALLOW_ALL = True
REST_SESSION_LOGIN = True
REST_USE_JWT = True
ACCOUNT_LOGOUT_ON_GET = True


LOCAL_APPS = (
    'project_name.apps.user.apps.UserConfig',
    'project_name.apps.core.apps.CoreConfig',
    'project_name.apps.module.apps.ModuleConfig',
    'project_name.apps.userprofile.apps.UserprofileConfig',


)

INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRD_PARTY_APPS

MIDDLEWARE = (
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.cache.UpdateCacheMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'project_name.apps.core.middleware.current_user.UserMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'project_name.apps.core.middleware.current_audit.AuditMiddleware',
)

ROOT_URLCONF = 'project_name.config.urls'

RAW_TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            str(PROJECT_ROOT.path('templates')),
        ],
        'OPTIONS': {
            'debug': DEBUG,
            'loaders': RAW_TEMPLATE_LOADERS,
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'project_name.config.wsgi.application'

# Password validation
#
# AUTH_PASSWORD_VALIDATORS = [
#     {
#         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#     },
# ]

# Internationalization
LANGUAGES = [
    ('es', _('Spanish')),
    ('en', _('English'))
]

LANGUAGE_CODE = 'en'

LOCALE_PATHS = (
    str(PROJECT_ROOT.path('locale')),
)

FIXTURE_DIR = (
    str(PROJECT_ROOT.path('fixture')),
)

SITE_ID = 1

TIME_ZONE = 'America/Lima'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATICFILES_DIRS = [
    str(PROJECT_ROOT.path('static')),
]

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

STATIC_ROOT = str(PROJECT_ROOT.path('run/static'))
MEDIA_ROOT = str(PROJECT_ROOT.path('run/media'))

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

AUTH_USER_MODEL = 'user.User'
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'

LOGOUT_REDIRECT_URL = '/login/'

ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True


LOGGING_DIR = str(PROJECT_ROOT.path('log'))
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(asctime)s %(levelname)s %(name)s %(module)s %(process)d %(thread)d  %(message)s'
        },
        'timestamped': {
            'format': '%(asctime)s %(levelname)s %(name)s  %(message)s'
        },
        'simple': {
            'format': '%(levelname)s  %(message)s'
        },
        'performance': {
            'format': '%(asctime)s %(process)d | %(thread)d | %(message)s',
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        },
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'timestamped'
        },
        'django': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': str(PROJECT_ROOT.path('log/django.log')),
            'formatter': 'verbose',
            'maxBytes': 1024 * 1024 * 10,  # 10 MB
            'backupCount': 10
        },
        'project': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': str(PROJECT_ROOT.path('log/project_name.log')),
            'formatter': 'verbose',
            'maxBytes': 1024 * 1024 * 10,  # 10 MB
            'backupCount': 10
        },
        'performance': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOGGING_DIR, 'performance.log'),
            'formatter': 'performance',
            'maxBytes': 1024 * 1024 * 10,  # 10 MB
            'backupCount': 10
        },
    },
    'loggers': {
        '{{ project_name|lower }}': {
            'handlers': ['project'],
            'level': 'INFO',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.template': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        },
    }
}

SECRET_FILE = str(PROJECT_ROOT.path('security/SECRET.key'))
try:
    from django.utils.crypto import get_random_string

    chars = 'abcdefghijklmnopqrstuvwxyz0123456789!$%&()=+-_'
    SECRET_KEY = get_random_string(50, chars)
    with open(SECRET_FILE, 'w') as f:
        f.write(SECRET_KEY)
        f.close()
except IOError:
    raise Exception('Could not open %s for writing!' % SECRET_FILE)
