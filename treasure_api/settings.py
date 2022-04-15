"""
Django settings for treasure_api project.

Generated by 'django-admin startproject' using Django 4.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import dj_database_url # add this
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # edit this var


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-nxi^gus^aeddt=q%hyipe2^0kd02ilg2ifnli07-tj&k%afar)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', 'treasure-trash-api.herokuapp.com', '*']


# Application definition

INSTALLED_APPS = [
    'corsheaders',
    'rest_framework',
    # 'rest_framework.authtoken', # new
    # 'rest_auth', # new
    # 'django.contrib.sites', # new
    # 'allauth', # new
    # 'allauth.account', # new
    # 'allauth.socialaccount', # new
    # 'rest_auth.registration', # new
    'items_api', #items app = free stuff
    # 'users', #users app
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', 
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

CORS_ALLOW_ALL_ORIGINS = True # add this



ROOT_URLCONF = 'treasure_api.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'treasure_api.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # }
    'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME': 'treasure_img_api',
       'USER': 'postgres',
       'PASSWORD': '666b',
       'HOST': 'localhost'
   }

}
db_from_env = dj_database_url.config(conn_max_age=600) # add this
DATABASES['default'].update(db_from_env) # add this


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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') # add this

#adding this:
STATICFILES_DIRS = (
  os.path.join(BASE_DIR, 'build/static'),
  os.path.join(BASE_DIR, 'build/media'),
  os.path.join(BASE_DIR, 'media/images')
  )
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# # Base url to serve media files
#directs the url to the media folder where our images will be
MEDIA_URL = '/media/'

# # Path where media is stored
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# #user model
# AUTH_USER_MODEL = 'users.CustomUser'
# # Django All Auth config. Add all of this.
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# AUTHENTICATION_BACKENDS = (    "django.contrib.auth.backends.ModelBackend",    "allauth.account.auth_backends.AuthenticationBackend",
# )

# SITE_ID = 1 
# ACCOUNT_EMAIL_REQUIRED = True
# ACCOUNT_USERNAME_REQUIRED = False
# ACCOUNT_SESSION_REMEMBER = True
# ACCOUNT_AUTHENTICATION_METHOD = 'email'
# ACCOUNT_UNIQUE_EMAIL = True
# # Rest Framework config. Add all of this.
# REST_FRAMEWORK = {    
# 'DATETIME_FORMAT': "%m/%d/%Y %I:%M%P",    'DEFAULT_AUTHENTICATION_CLASSES': [        'rest_framework.authentication.TokenAuthentication',    
# ],
# }
