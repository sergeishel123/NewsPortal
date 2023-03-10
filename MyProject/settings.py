"""
Django settings for MyProject project.

Generated by 'django-admin startproject' using Django 4.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
from pathlib import Path
import os
from django.core.mail import send_mail

from django.core.mail import mail_admins

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'dj-in-dsnmvkewjopwco-fdfkfdovdjvlx_fbmsklwpvkcbikpdsmpewalxnzkad4h59f*u38#8=gk1z@g%9%3$7!x+28s&e-op-xevl9gdyx7b81f'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']
ADMINS = [('agaverdyevsergej','agaverdyevsergej@gmail.com')]


# Application definition

INSTALLED_APPS = [
    'modeltranslation',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.flatpages',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'NewsPortal',
    'django_filters',
    'django_apscheduler',
    'rest_framework',

]
SITE_ID = 1
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'NewsPortal.middlewares.TimezoneMiddleware'
]
ROOT_URLCONF = 'MyProject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]

WSGI_APPLICATION = 'MyProject.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale')
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'ru'

LANGUAGES = [
    ('ru','??????????????'),
    ('en-us','English'),
]

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_DIRS = [
    BASE_DIR / "static"
]

LOGIN_REDIRECT_URL = '/news'

LOGIN_URL = '/accounts/login/'

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = True

ACCOUNT_FORM = {'signup': 'NewsPortal.models.CommonSignupForm'}

EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'sergeiazharkov'
EMAIL_HOST_PASSWORD = 'Agaver358'
EMAIL_USE_SSL = True
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER + '@yandex.ru'



# ???????????? ????????, ?????????????? ?????????? ???????????????????????? ?????? ???????????????? (???????????????????? ???????????? ???? ????????????????)
APSCHEDULER_DATETIME_FORMAT = "N j, Y, f:s a"

# ???????? ???????????? ???? ?????????????????????? ???? 25 ????????????, ???? ?????? ?????????????????????????? ??????????????????, ???????????? ?????????????????? ?????????? ????????????????, ???? ?????? ??????????????, ?????? ???????????? ???????? ???? ???????????????????????????????????? ??????????????
APSCHEDULER_RUN_NOW_TIMEOUT = 25  # Seconds

R_LOGIN = 'Agaver'
R_PSWD = 'Agaver123!'
R_HOST = 'redis-10238.c278.us-east-1-4.ec2.cloud.redislabs.com'
R_PORT = '10238'
broker = f"redis://{R_LOGIN}:{R_PSWD}@{R_HOST}:{R_PORT}/0"

CELERY_BROKER_URL = broker  # 'redis://:Agaver123!@redis-10238.c278.us-east-1-4.ec2.cloud.redislabs.com:10238/0'
CELERY_RESULT_BACKEND = broker  # 'redis://:Agaver123!@redis-10238.c278.us-east-1-4.ec2.cloud.redislabs.com:10238/0'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(BASE_DIR, 'cache_files')
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'style': '{',
    'formatters': {
        'simple': {
            'format': '%(asctime)s - %(levelname)s - %(message)s'
        },
        'simple_Warning': {
            'format': '%(asctime)s - %(levelname)s - %(message)s - %(pathname)s'
        },
        'simple_Error': {
            'format': '%(asctime)s - %(levelname)s - %(message)s - %(pathname)s - %(exc_info)s'
        },
        'simple_general': {
            'format': '%(asctime)s - %(levelname)s - %(module)s - %(message)s'
        },
        'simple_errors': {
            'format': '%(asctime)s - %(levelname)s - %(message)s - %(pathname)s - %(exc_info)s'
        },
        'simple_security': {
            'format': '%(asctime)s - %(levelname)s - %(module)s - %(message)s'
        },
        'simple_mail': {
            'format': '%(asctime)s - %(levelname)s - %(message)s - %(pathname)s'
        }

    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'console_Warninglevel': {
            'level': 'CRITICAL',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple_Warning'
        },
        'console_Errorlevel': {
            'level': 'ERROR',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple_Error'
        },
        'file_General': {
            'level': 'INFO',
            'filters': ['require_debug_false'],
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'simple_general',
            'filename': 'project_loggers.general.log',
            'maxBytes': 50000,
            'backupCount': 5
        },
        'file_Errors': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'simple_errors',
            'filename': 'project_loggers.errors.log',
            'maxBytes': 50000,
            'backupCount': 5
        },
        'file_Security': {
            'level': 'WARNING',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'simple_security',
            'filename': 'project_loggers.security.log',
            'maxBytes': 50000,
            'backupCount': 5
        },
        'mail_admins': {
            'level': 'WARNING',
            'class': 'django.utils.log.AdminEmailHandler',
            'filters': ['require_debug_false'],
            'formatter': 'simple_errors',

        }
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'console_Warninglevel', 'console_Errorlevel', 'file_General'],
            'propagate': True,
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.server': {
            'handlers': ['mail_admins','file_Errors',],
            'level': 'WARNING',
            'propagate': True
        },
        'django.template': {
            'handlers': ['file_Errors'],
            'level': 'WARNING',
            'propagate': True
        },
        'django.db.backends': {
            'handlers': ['file_Errors'],
            'level': 'ERROR',
            'propagate': True
        },
        'django.security': {
            'handlers': ['file_Security'],
            'level': 'WARNING',
            'propagate': True
        }


    }

}
