from pathlib import Path
from datetime import timedelta
import os
from dotenv import load_dotenv
load_dotenv()
get = os.getenv
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get("SECRET_KEY")
# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = not False

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    "user",
    "django.contrib.sites",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "corsheaders",
    "rest_framework",
    "rest_framework.authtoken",
    #"rest_framework_simplejwt",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "dj_rest_auth",
    'dj_rest_auth.registration',
    'coreapi', # Coreapi for coreapi documentation                                    
    'drf_yasg', # drf_yasg fro Swagger documentatio
   "upload",
    "order",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
     'whitenoise.middleware.WhiteNoiseMiddleware',
     "allauth.account.middleware.AccountMiddleware"
]

ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates/",],
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

WSGI_APPLICATION = 'backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    #'default': {
     #   'ENGINE': 'django.db.backends.mysql',
      #  'NAME': 'oop$default',
       # 'USER': 'oop',
       # 'PASSWORD': 'acsolotltd',
       # 'HOST': 'oop.mysql.pythonanywhere-services.com',
    #}
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
    
}

REST_FRAMEWORK = {                           
    'DEFAULT_AUTHENTICATION_CLASSES': ( 'dj_rest_auth.jwt_auth.JWTCookieAuthentication',),                                     
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
    'DEFAULT_PERMISSION_CLASSES': [
        #'rest_framework.permissions.IsAuthenticated',
    ],           
    }

REST_AUTH = {
    'LOGIN_SERIALIZER':  'user.models.CustomLoginSerializer',
    'REGISTER_SERIALIZER': 'user.models.CustomRegisterSerializer',
    "USER_DETAILS_SERIALIZER":'user.models.UserDetailsSerializer',
    "USE_JWT": True,
    'JWT_AUTH_RETURN_EXPIRATION': False,
    'JWT_AUTH_HTTPONLY':False
}
JWT_AUTH_RETURN_EXPIRATION =True
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=10),
    'REFRESH_TOKEN_LIFETIME': timedelta(hours=2),
    
    'TOKEN_OBTAIN_SERIALIZER': "user.models.CustomTokenObtainPairSerializer",
    "UPDATE_LAST_LOGIN": True,
    "TOKEN_REFRESH_SERIALIZER": "user.models.TokenRefreshSerializer",
}

ACCOUNT_AUTHENTICATION_METHOD = 'username_email'

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

AUTH_USER_MODEL = "user.User"
#USER_MODEL_USER_FIELD=None
ACCOUNT_USER_MODEL_USERNAME_FIELD = "email"
#ACCOUNT_USERNAME_REQUIRED=False
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD =  'email'# 'username_email'
ACCOUNT_EMAIL_VERIFICATION = "none" # 'mandatory'#

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT =  BASE_DIR /'static'

MEDIA_URL = '/media/'            
MEDIA_ROOT = BASE_DIR /'media'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CORS_ALLOWED_ORIGINS = [
     get("ALLOWED_ORIGINS")
]
CSRF_ALLOWED_ORIGINS = [
    get("ALLOWED_ORIGINS") 
]

SITE_ID=1
REST_USE_JWT=True

#fsao fbmc envo edwd
#STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = get("EMAIL_HOST_PASSWORD")
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False