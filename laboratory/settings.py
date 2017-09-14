import logging
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = 'sbib5ss_=z^qngyjqw1om5)4w5l@_ba@pin(7ee^k=#6q=0b)!'
DEBUG = "DLIS" in os.environ
INTERNAL_IPS = ['127.0.0.1', '192.168.0.200', '192.168.0.101', '192.168.102.4', '192.168.0.128']
ALLOWED_HOSTS = ['lis.fc-ismu.local', 'lis', '127.0.0.1', 'localhost', 'k165', 'k165.fc-ismu.local', '192.168.0.165', 'testserver']
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_HSTS_SECONDS = 1
X_FRAME_OPTIONS = 'ALLOWALL'
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admindocs',
    'cachalot',
    'ajax_select',
    'health',
    'appconf',
    'clients',
    'users',
    'dashboard',
    'podrazdeleniya',
    'results',
    'researches',
    'directions',
    'receivematerial',
    'construct',
    'slog',
    'directory',
    'statistic',
    'api',
    'discharge',
    'rmis_integration',
    'debug_toolbar',
    'debug_panel',
)
MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.admindocs.middleware.XViewMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'debug_panel.middleware.DebugPanelMiddleware',
    'django.middleware.common.CommonMiddleware',
]
ROOT_URLCONF = 'laboratory.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'), ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'djversion.context_processors.version',
                'context_processors.utils.card_bases',
            ]
        },
    },
]
WSGI_APPLICATION = 'laboratory.wsgi.application'
LOGIN_URL = '/'
LOGIN_REDIRECT_URL = '/dashboard/'
# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'l2',
        'USER': 'postgres',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
        'KEY_PREFIX': 'lis' + ("" if not DEBUG else "_DBG")
    },
    'debug-panel': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/var/tmp/debug-panel-cache-2',
        'TIMEOUT': 300,
        'OPTIONS': {
            'MAX_ENTRIES': 200
        }
    }
}
LANGUAGE_CODE = 'ru-ru'
DATE_FORMAT = 'd.m.Y'
TIME_FORMAT = 'd.m.Y'
USE_TZ = True
TIME_ZONE = 'Asia/Irkutsk'
USE_I18N = True
USE_L10N = True
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
FIXTURE_DIRS = (os.path.join(BASE_DIR, 'fixtures'),)
AUTH_PROFILE_MODULE = 'users.models.DoctorsProfile'
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'logs') + '/log.txt',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
DEBUG_TOOLBAR_PANELS = (
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'cachalot.panels.CachalotPanel',
)
LDAP = {
    "enable": False,
    "server": {
        "host": "192.168.0.254",
        "port": 389,
        "user": "cn=Admin,dc=fc-ismu,dc=local",
        "password": ""
    },
    "user_object": "(objectClass=*)",
    "base": "dc=fc-ismu,dc=local"
}
SESSION_SAVE_EVERY_REQUEST = True
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_COOKIE_AGE = 15 * 60 * 60
class DisableMigrations(object):
    def __contains__(self, item):
        return True
    def __getitem__(self, item):
        return "notmigrations"
TESTS_IN_PROGRESS = False
if 'test' in sys.argv[1:] or 'jenkins' in sys.argv[1:]:
    logging.disable(logging.CRITICAL)
    PASSWORD_HASHERS = (
        'django.contrib.auth.hashers.MD5PasswordHasher',
    )
    DEBUG = False
    TEMPLATE_DEBUG = False
    TESTS_IN_PROGRESS = True
    MIGRATION_MODULES = DisableMigrations()
import time, datetime
DJVERSION_VERSION = "1.0.0"
__w = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
if os.path.exists(__w):
    (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(__w)
    mtime = datetime.datetime.fromtimestamp(mtime)
    DJVERSION_UPDATED = mtime
DJVERSION_FORMAT_STRING = '{version}'
CACHALOT_ENABLED = True

import warnings
warnings.filterwarnings('ignore', message='DateTimeField*', category=RuntimeWarning)
MAX_UPLOAD_SIZE = DATA_UPLOAD_MAX_MEMORY_SIZE = 104857600

DEBUG = False

try:
    from laboratory.local_settings import *
except ImportError:
    pass