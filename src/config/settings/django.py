import os
from pathlib import Path
import toml


BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Connecting the Environment Variables
# _________________________________________________________
if os.path.exists(BASE_DIR / 'config.toml'):
    _config_path = 'config.toml'
elif os.path.exists(BASE_DIR / 'config_local.toml'):
    _config_path = 'config_local.toml'
else:
    _config_path = 'default_config.toml'
with open(BASE_DIR / _config_path, 'r') as f:
    config = toml.load(f)
# _________________________________________________________

# Basic settings from the Environment Variables
# _________________________________________________________
SECRET_KEY = config['base']['secret_key']
DEBUG = config['base']['debug']
ALLOWED_HOSTS = config['base']['allowed_hosts']
# _________________________________________________________


# Storage
# _________________________________________________________
STATIC_URL = config['storage']['static_url']
MEDIA_URL = config['storage']['media_url']

MEDIA_ROOT = config['storage']['media_root']
STATIC_ROOT = config['storage']['static_root']

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
# _________________________________________________________


# Database settings
# _________________________________________________________
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
# _________________________________________________________


# Basic settings
# _________________________________________________________
ROOT_URLCONF = 'config.urls'
WSGI_APPLICATION = 'config.wsgi.application'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# _________________________________________________________


# Language settings
# _________________________________________________________
LANGUAGE_CODE = 'en-us'
# _________________________________________________________


# Time settings
# _________________________________________________________
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True
# _________________________________________________________


# Apps settings
# _________________________________________________________
INSTALLED_APPS = [
    # Django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Libraries

    # Apps
    'apps.common.apps.CommonConfig',
]
# _________________________________________________________


# Middleware settings
# _________________________________________________________
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
# _________________________________________________________


# Templates settings
# _________________________________________________________
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
            ],
        },
    },
]
# _________________________________________________________


# Password validation settings
# _________________________________________________________
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
# _________________________________________________________
