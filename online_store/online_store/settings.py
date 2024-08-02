import os
from pathlib import Path
import dj_database_url
import django_heroku

# Base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Secret key management
SECRET_KEY = os.environ.get('SECRET_KEY', 'default-secret-key')

# Debug mode management
DEBUG = bool(os.environ.get('DEBUG', False))

# Allowed hosts management
ALLOWED_HOSTS = ['tenkaitechstore.herokuapp.com', 'localhost', '127.0.0.1']

# WSGI application path
WSGI_APPLICATION = 'online_store.wsgi.application'

# Configuración de la base de datos
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('DB_NAME', 'jkadc7qsm3d7j8dh'),  # Nombre de la base de datos
        'USER': os.environ.get('DB_USER', 'c71pl68bsle11pql'),  # Nombre de usuario
        'PASSWORD': os.environ.get('DB_PASSWORD', 'pfx0wcf6b0v5ih2s'),  # Contraseña
        'HOST': os.environ.get('DB_HOST', 'mgs0iaapcj3p9srz.cbetxkdyhwsb.us-east-1.rds.amazonaws.com'),  # Host
        'PORT': os.environ.get('DB_PORT', '3306'),  # Puerto
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"  # Opcional: Activa el modo estricto
        },
    }
}

# Installed applications
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'corsheaders',
    'store',
    'rest_framework',
]

# Middleware configuration
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

# Root URL configuration
ROOT_URLCONF = 'online_store.urls'

# Template settings
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'store', 'templates', 'store_templates')],
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

# CORS configuration
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://192.168.1.13:3000",
]

# Password validation
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

# Localization settings
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Media files configuration
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Static files configuration
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Opcional: Si necesitas incluir archivos estáticos adicionales del backend, puedes dejarlos aquí.
#STATICFILES_DIRS = [
    # Elimina esta línea si no tienes archivos estáticos específicos en `backend/static`.
    # os.path.join(BASE_DIR, 'backend/static'),
#]

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Activate Django-Heroku
django_heroku.settings(locals())
