"""
Django settings for the LoveLens project.

These settings configure various aspects of the Django project, including database settings,
static files, internationalization, and more.

For more information on Django settings, see:
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see:
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from os import path
from pathlib import Path
from django.core.management.utils import get_random_secret_key

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_random_secret_key()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ALLOWED_HOSTS = env("ALLOWED_HOSTS")
ALLOWED_HOSTS = ["*"]  # Only while in development

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    #
    "ckeditor",
    "ckeditor_uploader",
    "features.gallery",
    "features.members",
    "crispy_forms",
    "crispy_bootstrap5",
    "django_cleanup.apps.CleanupConfig",
    "django_seed",
    "django_currentuser",
]

# CK editor session #
CKEDITOR_UPLOAD_PATH = "content/ckeditor/"

CKEDITOR_CONFIGS = {
    "default": {
        "config.height": "full",
        "config.width": "full",
        # "skin": "moono-dark",
        "editorplaceholder": "Descrição da imagem...",
        "toolbar": [
            {
                "name": "document",
                "items": [
                    "Source",
                    "-",
                    "Preview",
                    "-",
                    "Templates",
                ],
            },
            {
                "name": "clipboard",
                "items": [
                    "Cut",
                    "Copy",
                    "Paste",
                    "PasteText",
                    "PasteFromWord",
                    "-",
                    "Undo",
                    "Redo",
                ],
            },
            {
                "name": "editing",
                "items": [
                    "Find",
                    "Replace",
                    "-",
                    "SelectAll",
                    "-",
                    "Scayt",
                ],
            },
            {
                "name": "basicstyles",
                "items": [
                    "Bold",
                    "Italic",
                    "Underline",
                    "Strike",
                    "Subscript",
                    "Superscript",
                    "-",
                    "RemoveFormat",
                ],
            },
            {
                "name": "paragraph",
                "items": [
                    "NumberedList",
                    "BulletedList",
                    "-",
                    "Blockquote",
                    "-",
                    "JustifyLeft",
                    "JustifyCenter",
                    "JustifyRight",
                    "JustifyBlock",
                ],
            },
            {
                "name": "links",
                "items": [
                    "Link",
                    "Unlink",
                    "Anchor",
                ],
            },
            {
                "name": "insert",
                "items": [
                    "Image",
                    "Flash",
                    "Table",
                    "HorizontalRule",
                    "Smiley",
                    "SpecialChar",
                    "Iframe",
                ],
            },
            {
                "name": "styles",
                "items": [
                    "Styles",
                    "Format",
                    "Font",
                    "FontSize",
                ],
            },
            {
                "name": "colors",
                "items": [
                    "TextColor",
                    "BGColor",
                ],
            },
            {
                "name": "tools",
                "items": [
                    "Maximize",
                    "ShowBlocks",
                ],
            },
            {
                "name": "about",
                "items": [
                    "About",
                ],
            },
        ],
    },
}

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django_currentuser.middleware.ThreadLocalUserMiddleware",
]

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
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

WSGI_APPLICATION = "core.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

LOGOUT_REDIRECT_URL = "login_user"
LOGIN_REDIRECT_URL = "home_page"
# SIGNUP_REDIRECT_URL = "login_user"


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "pt-br"

TIME_ZONE = "America/Sao_Paulo"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "/static/"
STATICFILES_DIRS = [path.join(BASE_DIR, "static")]
STATIC_ROOT = BASE_DIR / "static_django"

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

# ╔───────────────────────────────────────────────╗ #
# │▒███████▒ ██▓ █    ██   ▄████  ▒█████  ▓█████▄ │ #
# │▒ ▒ ▒ ▄▀░▓██▒ ██  ▓██▒ ██▒ ▀█▒▒██▒  ██▒▒██▀ ██▌│ #
# │░ ▒ ▄▀▒░ ▒██▒▓██  ▒██░▒██░▄▄▄░▒██░  ██▒░██   █▌│ #
# │  ▄▀▒   ░░██░▓▓█  ░██░░▓█  ██▓▒██   ██░░▓█▄   ▌│ #
# │▒███████▒░██░▒▒█████▓ ░▒▓███▀▒░ ████▓▒░░▒████▓ │ #
# │░▒▒ ▓░▒░▒░▓  ░▒▓▒ ▒ ▒  ░▒   ▒ ░ ▒░▒░▒░  ▒▒▓  ▒ │ #
# │░░▒ ▒ ░ ▒ ▒ ░░░▒░ ░ ░   ░   ░   ░ ▒ ▒░  ░ ▒  ▒ │ #
# │░ ░ ░ ░ ░ ▒ ░ ░░░ ░ ░ ░ ░   ░ ░ ░ ░ ▒   ░ ░  ░ │ #
# │  ░ ░     ░     ░           ░     ░ ░     ░    │ #
# ╚───────────────────────────────────────────────╝ #
