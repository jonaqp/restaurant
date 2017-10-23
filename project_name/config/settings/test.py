from .settings import *

env_file = str(PROJECT_ROOT.path('security/environ_local.env'))
environ.Env.read_env(str(env_file))

ALLOWED_HOSTS = ["*"]


DEBUG = False
WSGI_APPLICATION = 'project_name.config.wsgi.test.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'project_name',
        'USER': 'project_name',
        'PASSWORD': 'project_name',
        'HOST': '127.0.0.1',
        'PORT': '5432',
        'TEST': {
            'NAME': 'test_%s' % env('JOB_NAME', default='project_name')
        }
    }
}

INSTALLED_APPS += (
    'django_jenkins',
)

PROJECT_APPS = [app for app in INSTALLED_APPS if app.startswith('project_name')]

JENKINS_TASKS = (
    'django_jenkins.tasks.run_pylint',
    'django_jenkins.tasks.run_pep8',
)


# https://www.google.com/settings/security/lesssecureapps
EMAIL_BACKEND = env('DJANGO_EMAIL_BACKEND')
EMAIL_CONFIG = env.email_url('EMAIL_URL')
vars().update(EMAIL_CONFIG)

ADMIN_URL = env('ADMIN_URL')

LOGGING['loggers'].update({
    'django': {
        'handlers': ['django'],
        'level': 'WARNING',
        'propagate': True,
    },
})
