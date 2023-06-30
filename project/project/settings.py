"""
Django's settings for project.

Generated by 'django-admin startproject' using Django 4.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-0636k4m&cq@$yb=((kwads)15#ex2ln=%ccpsrsev919%1c_im'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'project',
    'simpleapp',
    'django_filters',
    #'django.contrib.site`s',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.yandex',
    #'new'
    #'NewsPortal',
]

CACHES = {
    'default': {
        'TIMEOUT': 60, # добавляем стандартное время ожидания в минуту (по умолчанию это 5 минут — 300 секунд)
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(BASE_DIR, 'cache_files'), # Указываем, куда будем сохранять кэшируемые файлы! Не забываем создать папку cache_files внутри папки с manage.py!
    }
}

CELERY_BROKER_URL = 'redis://default:9UMLfVTMbvUoOYGVHwWgpHsfcccQvMd8@redis-19516.c81.us-east-1-2.ec2.cloud.redislabs.com:19516'
CELERY_RESULT_BACKEND = 'redis://default:9UMLfVTMbvUoOYGVHwWgpHsfcccQvMd8@redis-19516.c81.us-east-1-2.ec2.cloud.redislabs.com:19516'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'


ACCOUNT_FORMS = {"signup": "accounts.forms.CustomSignupForm"}

LOGIN_REDIRECT_URL = "/products"


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',


    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
]

SITE_ID = 1

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
            ],
        },
    },
]



ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'none'
ACCOUNT_FORMS = {'signup': 'accounts.forms.CustomSignupForm'}


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'  # для отправки писем на реальные почтовые адреса
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  # Для тестирования, печать писем в консоль.
EMAIL_HOST = 'smtp.yandex.ru'                                # хост почтового сервера
EMAIL_PORT = 465                                             # порт, на который почтовый сервер принимает письма
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')          # логин пользователя почтового сервера
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')  # пароль пользователя почтового сервера
EMAIL_USE_TLS = False                                    # необходимость использования TLS (зависит от почтового сервера
EMAIL_USE_SSL = True                                     # необходимость использования SSL (зависит от почтового сервера

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

WSGI_APPLICATION = 'project.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_DIRS = [
    BASE_DIR / "static"
]



LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'form_debug': {
            'format': '{asctime} - [{levelname}] - {message}',
            'style': '{',
        },  # 1

        'form_warning_mail': {
            'format': '{asctime} - [{levelname}] - {message} - {pathname} ',
            'style': '{',
        },  # 1 и 5

        'form_error': {
            'format': '{asctime} - [{levelname}] - {message} - {pathname} - {exc_info} ',
            'style': '{',
        },  # 1 и 3

        'general_security_info': {
            'format': '{asctime} - [{levelname}] - {message} - {module} ',
            'style': '{',
        },  # 2 и 4
    },

    'handlers': {
        'console_d': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'form_debug',
        },  # 1

        'console_w': {
            'level': 'WARNING',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'form_warning_mail',
        },  # 1

        'console_e': {
            'level': 'ERROR',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'form_error',
        },  # 1

        'general_hand': {
            'level': 'INFO',
            'filters': ['require_debug_false'],
            'class': 'logging.FileHandler',
            'formatter': 'general_security_info',
            'filename': 'general.log',
        },  # 2

        'errors_hand': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'formatter': 'form_error',
            'filename': 'errors.log',
        },  # 3

        'security_hand': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'formatter': 'general_security_info',
            'filename': 'security.log',
        },  # 4

        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter': 'form_warning_mail',
        },  # 5
    },

    'filters': {
        'require_debug_true': {'()': 'django.utils.log.RequireDebugTrue'},  # 1 х3
        'require_debug_false': {'()': 'django.utils.log.RequireDebugFalse'},  # 5 и 2
    },

    'loggers': {
        'django': {
            'handlers': ['console_d', 'console_w', 'console_e', 'general_hand', ],
            'level': 'DEBUG',
            'propagate': True,
        },  # 1 и 2

        'django.request': {
            'handlers': ['errors_hand', 'mail_admins', ],
            'level': 'ERROR',
            'propagate': False,
        },  # 3 и 5

        'django.server': {
            'handlers': ['errors_hand', 'mail_admins', ],
            'level': 'ERROR',
            'propagate': False,
        },  # 3 и 5

        'django.template': {
            'handlers': ['errors_hand', ],
            'level': 'ERROR',
            'propagate': True,
        },  # 3

        'django.db.backends': {
            'handlers': ['errors_hand', ],
            'level': 'ERROR',
            'propagate': True,
        },  # 3

        'django.security': {
            'handlers': ['security_hand', ],
            'level': 'INFO',
            'propagate': False,
        },  # 4
    }
}