# -*- coding: utf-8 -*-
"""
Django settings for tarjimonlar project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from os.path import join, dirname

from configurations import Configuration, values
from getenv import env

BASE_DIR = dirname(dirname(__file__))


class Common(Configuration):

    # APP CONFIGURATION
    DJANGO_APPS = (
        # Default Django apps:
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.sites',
        'django.contrib.messages',
        'django.contrib.staticfiles',

        # Useful template tags:
        'django.contrib.humanize',

        # Admin
        'django.contrib.admin',
    )
    THIRD_PARTY_APPS = (
        'crispy_forms',  # Form layouts
        'avatar',  # for user avatars
        'pipeline', # minimize assets
        'haystack',
        'django_facebook',
    )

    # Apps specific for this project go here.
    LOCAL_APPS = (
        'core',
        # Your stuff: custom apps go here
    )

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
    INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
    # END APP CONFIGURATION

    # MIDDLEWARE CONFIGURATION
    MIDDLEWARE_CLASSES = (
        # Make sure djangosecure.middleware.SecurityMiddleware is listed first
        'djangosecure.middleware.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        'django.middleware.gzip.GZipMiddleware',
        'pipeline.middleware.MinifyHTMLMiddleware',
    )
    # END MIDDLEWARE CONFIGURATION

    # MIGRATIONS CONFIGURATION
    MIGRATION_MODULES = {
        'sites': 'contrib.sites.migrations'
    }
    # END MIGRATIONS CONFIGURATION

    # DEBUG
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
    DEBUG = values.BooleanValue(False)

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
    TEMPLATE_DEBUG = DEBUG
    # END DEBUG

    # SECRET CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
    # Note: This key only used for development and testing.
    #       In production, this is changed to a values.SecretValue() setting
    SECRET_KEY = 'CHANGEME!!!'
    # END SECRET CONFIGURATION

    # FIXTURE CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-FIXTURE_DIRS
    FIXTURE_DIRS = (
        join(BASE_DIR, 'fixtures'),
    )
    # END FIXTURE CONFIGURATION

    # EMAIL CONFIGURATION
    EMAIL_BACKEND = values.Value('django.core.mail.backends.smtp.EmailBackend')
    # END EMAIL CONFIGURATION

    # MANAGER CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#admins
    ADMINS = (
        ("""Sardor Muminov""", 'smuminov@gmail.com'),
    )

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#managers
    MANAGERS = ADMINS
    # END MANAGER CONFIGURATION

    # DATABASE CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
    DATABASES = values.DatabaseURLValue('postgres://tarjimonlar:tarjimonlar@localhost/tarjimonlar')
    # DATABASES = values.DatabaseURLValue('sqlite:///master.db')
    # END DATABASE CONFIGURATION

    # CACHING
    # Do this here because thanks to django-pylibmc-sasl and pylibmc
    # memcacheify (used on heroku) is painful to install on windows.
    SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
    CACHES = {
        "default": {
            "BACKEND": "django_redis.cache.RedisCache",
            "LOCATION": "redis://127.0.0.1:6379/1",
            "OPTIONS": {
                "CLIENT_CLASS": "django_redis.client.DefaultClient",
            }
        }
    }
    # END CACHING

    # GENERAL CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#time-zone
    TIME_ZONE = 'Asia/Tashkent'

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#language-code
    LANGUAGE_CODE = 'uz-uz'

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#site-id
    SITE_ID = 2

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
    USE_I18N = True

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
    USE_L10N = True

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
    USE_TZ = True
    # END GENERAL CONFIGURATION

    # TEMPLATE CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
    TEMPLATE_CONTEXT_PROCESSORS = (
        'django.contrib.auth.context_processors.auth',
        'django.core.context_processors.debug',
        'django.core.context_processors.i18n',
        'django.core.context_processors.media',
        'django.core.context_processors.static',
        'django.core.context_processors.tz',
        'django.contrib.messages.context_processors.messages',
        'django.core.context_processors.request',
        'django_facebook.context_processors.facebook',
        'core.context_processors.navbar',
        # Your stuff: custom template context processers go here
    )

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
    TEMPLATE_DIRS = (
        join(BASE_DIR, 'templates'),
    )

    TEMPLATE_LOADERS = (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )

    # See: http://django-crispy-forms.readthedocs.org/en/latest/install.html#template-packs
    CRISPY_TEMPLATE_PACK = 'bootstrap3'
    # END TEMPLATE CONFIGURATION

    # STATIC FILE CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
    STATIC_ROOT = join(os.path.dirname(BASE_DIR), 'staticfiles')

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
    STATIC_URL = '/static/'

    # See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
    STATICFILES_DIRS = (
        join(BASE_DIR, 'static'),
    )

    # See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
    STATICFILES_FINDERS = (
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
        'pipeline.finders.PipelineFinder',
        'pipeline.finders.CachedFileFinder',
    )
    # END STATIC FILE CONFIGURATION

    # MEDIA CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
    MEDIA_ROOT = join(BASE_DIR, 'media')

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url
    MEDIA_URL = '/media/'
    # END MEDIA CONFIGURATION

    # URL Configuration
    ROOT_URLCONF = 'deploy.urls'

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
    WSGI_APPLICATION = 'deploy.wsgi.application'
    # End URL Configuration

    # AUTHENTICATION CONFIGURATION
    AUTHENTICATION_BACKENDS = (
        'django.contrib.auth.backends.ModelBackend',
        'django_facevook.auth.backends.FacebookBackend',
    )

    AUTH_USER_MODEL = 'django_facebook.FacebookCustomUser'
    AUTH_PROFILE_MODEL = 'django_facebook.FacebookProfile'

    # SLUGLIFIER
    AUTOSLUG_SLUGIFY_FUNCTION = 'slugify.slugify'
    # END SLUGLIFIER

    # LOGGING CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#logging
    # A sample logging configuration. The only tangible logging
    # performed by this configuration is to send an email to
    # the site admins on every HTTP 500 error when DEBUG=False.
    # See http://docs.djangoproject.com/en/dev/topics/logging for
    # more details on how to customize your logging configuration.
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'filters': {
            'require_debug_false': {
                '()': 'django.utils.log.RequireDebugFalse'
            }
        },
        'handlers': {
            'mail_admins': {
                'level': 'ERROR',
                'filters': ['require_debug_false'],
                'class': 'django.utils.log.AdminEmailHandler'
            }
        },
        'loggers': {
            'django.request': {
                'handlers': ['mail_admins'],
                'level': 'ERROR',
                'propagate': True,
            },
        }
    }
    # END LOGGING CONFIGURATION

    @classmethod
    def post_setup(cls):
        cls.DATABASES['default']['ATOMIC_REQUESTS'] = True

    # Your common stuff: Below this line define 3rd party library settings
    PIPELINE_CSS = {
        'flat': {
            'source_filenames': (
                'css/flat.css',
            ),
            'output_filename': 'css/flat.min.css',
        },
        'project': {
            'source_filenames': (
                'uncss/project.css',
            ),
            'output_filename': 'css/project.min.css',
        },
        'bootstrap': {
            'source_filenames': (
                'uncss/bootstrap.css',
            ),
            'output_filename': 'css/bootstrap.min.css',
        },
        'chart': {
            'source_filenames': (
                'uncss/chart.css',
            ),
            'output_filename': 'css/chart.min.css',
        },
    }
    PIPELINE_JS = {
        'modernizr': {
            'source_filenames': (
                'js/modernizr.js',
            ),
            'output_filename': 'js/modernizr.min.js',
        },
        'jquery': {
            'source_filenames': (
                'js/jquery.js',
            ),
            'output_filename': 'js/jquery.min.js',
        },
        'jquery_gridrotator': {
            'source_filenames': (
                'js/jquery.gridrotator.js',
            ),
            'output_filename': 'js/jquery.gridrotator.js',
        },
        'bootstrap': {
            'source_filenames': (
                'js/bootstrap.js',
            ),
            'output_filename': 'js/bootstrap.min.js',
        },
        'flat': {
            'source_filenames': (
                'js/flat.js',
            ),
            'output_filename': 'js/flat.min.js',
        },
        'project': {
            'source_filenames': (
                'js/project.js',
            ),
            'output_filename': 'js/project.min.js',
        },
        'raphael': {
            'source_filenames': (
                'js/raphael.js',
            ),
            'output_filename': 'js/raphael.min.js',
        },
        'morris': {
            'source_filenames': (
                'js/morris.js',
            ),
            'output_filename': 'js/morris.min.js',
        },
        'halloffame': {
            'source_filenames': (
                'js/halloffame.js',
            ),
            'output_filename': 'js/halloffame.min.js',
        },
        'posts_chart': {
            'source_filenames': (
                'js/posts_chart.js',
            ),
            'output_filename': 'js/posts_chart.min.js',
        },
        'comments_chart': {
            'source_filenames': (
                'js/comments_chart.js',
            ),
            'output_filename': 'js/comments_chart.min.js',
        },
    }
    PIPELINE_CSS_COMPRESSOR = 'pipeline.compressors.yuglify.YuglifyCompressor'
    PIPELINE_JS_COMPRESSOR = 'pipeline.compressors.jsmin.JSMinCompressor'
    # STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'
    PIPELINE_VERSIONING = 'pipeline.versioning.hash.MD5Versioning'
    PIPELINE_ENABLED = True
    PIPELINE_AUTO = True
    PIPELINE_VERSION = True
    AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = env('AWS_STORAGE_BUCKET_NAME')
    AWS_QUERYSTRING_AUTH = False
    AWS_IS_GZIPPED = True
    AWS_HEADERS = {
            'Cache-Control': 'max-age=86400',
            }
    STATICFILES_STORAGE = 'core.storage.S3PipelineStorage'

    # Haystack
    HAYSTACK_CONNECTIONS = {
            'default': {
                'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
                'URL': 'http://127.0.0.1:9200/',
                'INDEX_NAME': 'haystack',
                },
            }
    HAYSTACK_SEARCH_RESULTS_PER_PAGE = 10
    FACEBOOK_APP_ID = env('FACEBOOK_APP_ID')
    FACEBOOK_APP_SECRET = env('FACEBOOK_APP_SECRET')
