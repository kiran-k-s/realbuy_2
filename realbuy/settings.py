import os

from pathlib import Path
#import django_heroku    #heroku deploy

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$m_xqhsgx&fk%l#2j5#1#$zag((y4^5+h^7=jdv@@$aeg3c&n%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'realbuy_app',
    'members',
    'multiselectfield',
    'select2',
    'bootstrap_modal_forms',
    'social_django',
    'django.contrib.humanize',  
    'django.contrib.sites',   # for allauth
    'django_social_share',
    'django_google_maps',
    #allauth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    #providers
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.twitter',

]
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  # During development only



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',     #heroku_deploy
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'social_django.middleware.SocialAuthExceptionMiddleware',   #social_authentication
]

ROOT_URLCONF = 'realbuy.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                

                #'social_django.context_processors.backends',        #social_authentication
                #'social_django.context_processors.login_redirect',

            ],
        },
    },
]
        #social-authentication
'''        
AUTHENTICATION_BACKENDS = (
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.google.GoogleOAuth',

    'django.contrib.auth.backends.ModelBackend',
)'''

WSGI_APPLICATION = 'realbuy.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
       # 'NAME': BASE_DIR / 'db.sqlite3',
        'NAME': 'realbuydb',
        'USER': 'postgres',
        'PASSWORD' : 'kiran@123',
        'HOST': 'localhost',
        'PORT': '5432',
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
#BASE_DIR = os.path.dirname(os.path.abspath(__file__))        #heroku deploy

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/' 
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

#django_heroku.settings(locals())       #activate django heroku

'''EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'realbuy1983@gmail.com'
EMAIL_HOST_PASSWORD = 'udsndagmpavfqljm'
EMAIL_USE_TLS = True  '''
#LOGIN_URL = 'login_page'
#LOGIN_REDIRECT = 'add1' 
#LOGOUT_URL = 'logout'
LOGOUT_REDIRECT_URL = 'home' 

#heroku deploy
'''
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

import os
from decouple import config,Csv
import dj_database_url
from dj_database_url import config



SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', cast=bool)
DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL')
    )
} 
'''
'''
SOCIAL_AUTH_FACEBOOK_KEY = '255371952605641'  # App ID
SOCIAL_AUTH_FACEBOOK_SECRET = '510dc754cb356b1319cd5855acad5597'  # App Secret
SESSION_COOKIE_SECURE=False
SOCIAL_AUTH_TWITTER_KEY = '9TD8f5fhasdsbf4w61GSM9' 
SOCIAL_AUTH_TWITTER_SECRET = 'mwtdcUe4uOvvjDk2Ausb45gsasdasdasashw65454TNSx' 
SOCIAL_AUTH_GOOGLE_KEY = '652793475567-c9j1s8hfv8io16heb1mub1ek91m1id91.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_SECRET = 'BUIe7RnyCmTmGAf_LwegKAUE'  '''


SITE_ID = 1  #allauth

LOGIN_REDIRECT_URL = 'add1'