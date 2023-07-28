import os
import sys
import yaml

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-vj(hm@^=wqulw3n=(u5@m+iwc#1n%ngl5s)lu1j3-*jpx1=9!4"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "corsheaders",
    "drf_yasg",
    "rest_framework",
    "django_filters",

    "apps.plans.apps.PlansConfig",
    "apps.tasks.apps.TasksConfig",
]

CORS_ORIGIN_ALLOW_ALL = True  # 指定所有域名都可以访问后端接口
CORS_ALLOW_CREDENTIALS = True  # 允许跨域时携带Cookie

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    'corsheaders.middleware.CorsMiddleware',  # 解决跨站访问问题
    "django.middleware.common.CommonMiddleware",
    # "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "smartest.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / 'templates'],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "smartest.wsgi.application"

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
CONF_FILE = os.path.join(BASE_DIR, "conf/database.yaml")
DATABASES = yaml.load(open(CONF_FILE, "r", encoding="UTF-8"), Loader=yaml.FullLoader)

DATABASES_APPS_MAPPING = {
    "apps.plans.apps.PlansConfig": "smartest_mysql",
    "apps.tasks.apps.TasksConfig": "smartest_mongo",
}

DATABASE_ROUTERS = ["utils.app_router.DatabaseAppsRouter"]

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "zh-hans"

TIME_ZONE = "Asia/Shanghai"

USE_I18N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/
RUNTIME_URL = "runtime/"
RUNTIME_ROOT = os.path.join(BASE_DIR, RUNTIME_URL)
os.makedirs(RUNTIME_ROOT, exist_ok=True)

STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, STATIC_URL)
os.makedirs(STATIC_ROOT, exist_ok=True)

MEDIA_URL = 'upload/'
MEDIA_ROOT = os.path.join(BASE_DIR, MEDIA_URL)
os.makedirs(MEDIA_ROOT, exist_ok=True)

LOG_RUL = 'logs/'
LOG_ROOT = os.path.join(RUNTIME_ROOT, LOG_RUL)
os.makedirs(LOG_ROOT, exist_ok=True)

SMART_LOG_FILE = os.path.join(LOG_ROOT, 'smartest.log')

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {
            "class": "logging.Formatter",
            "format": "[%(asctime)s][%(name)s][%(levelname)s] [%(process)d] [%(filename)s:%(lineno)d] %(message)s"
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "INFO",
            "formatter": "simple",
            "stream": "ext://sys.stdout",
        },
        "smartest": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "INFO",
            "formatter": "simple",
            "filename": SMART_LOG_FILE,
            "maxBytes": 10485760,
            "backupCount": 50,
            "encoding": "utf8",
        }
    },
    "loggers": {
        "django": {
            "handlers": ["console", "smartest"],
            "level": "INFO"
        }
    }
}

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.backends.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter'
    ],  # 默认过滤引擎
    'DEFAULT_PAGINATION_CLASS': 'utils.pagination.PageNumberPaginationManual',  # 全局指定分页的引擎

    # 'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
    #
    # # 认证类
    # 'DEFAULT_AUTHENTICATION_CLASSES': [
    #     'rest_framework_jwt.authentication.JSONWebTokenAuthentication',  # token认证 第三方jwt认证方式
    #     'rest_framework.authentication.SessionAuthentication',
    #     'rest_framework.authentication.BasicAuthentication'
    # ],
    # 授权类
    # 'DEFAULT_PERMISSION_CLASSES': [
    #     'rest_framework.permissions.AllowAny',
    # ],
}
