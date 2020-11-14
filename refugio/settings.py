import os
from pathlib import Path
from django.urls import reverse_lazy
import mimetypes


mimetypes.add_type("text/css", ".css", True)

WHITENOISE_MIMETYPES = {
    '.xsl': 'application/xml'
}

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = '3l#ucg65k)&(_0r&hc87dicn!c3(1yal1&7t*4w7_9)wf384or'
DEBUG = True
ALLOWED_HOSTS = []

GOOGLE_MAPS_API_KEY = 'AIzaSyDZktO_JnnvrY4BnD2IyZo8PqNXiDTWP1w'

INSTALLED_APPS = [
    'django_google_maps',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.adopcion',
    'apps.mascota',
    'apps.usuario',
    'apps.googlemaps',
    'bootstrap4',
    'rest_framework'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'refugio.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'refugio.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'refugio',
        'USER': 'root',
        'PASSWORD': '',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'es-pe'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

# https://docs.djangoproject.com/en/3.1/howto/static-files/


STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'),]

# STATIC_ROOT  = os.path.join(BASE_DIR, 'static')

LOGIN_REDIRECT_URL = reverse_lazy('solicitud_listar')
LOGOUT_REDIRECT_URL = reverse_lazy('login') 


EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'migmail@gmail.com'
EMAIL_HOST_PASSWORD = 'micontrasenia'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
