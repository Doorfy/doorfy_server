#coding: utf-8
# Django settings for doorfy_server project.
import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG
SITE_ROOT = os.path.realpath(os.path.dirname(__file__))

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',       # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'doorfy',                           # Or path to database file if using sqlite3.
        'USER': 'root',                             # Not used with sqlite3.
        'PASSWORD': 'hello1234',                    # Not used with sqlite3.
        'HOST': '127.0.0.1',                        # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '3306',                             # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Asia/Shanghai'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(SITE_ROOT, 'static')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
    'compressor.finders.CompressorFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = ''

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.gzip.GZipMiddleware',
)

ROOT_URLCONF = 'doorfy_server.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'doorfy_server.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(SITE_ROOT, 'templates'),
)

INSTALLED_APPS = (
    'doorfy_server.hacks',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    # 'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'compressor',
    'doorfy_server.account',
    'doorfy_server.family',
    'captcha',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '[%(levelname)s] %(asctime)-15s %(message)s'
        },
    },
    'handlers': {
        # Include the default Django email handler for errors
        # This is what you'd get without configuring logging at all.
        'mail_admins': {
            'class': 'django.utils.log.AdminEmailHandler',
            'level': 'ERROR',
             # But the emails are plain text by default - HTML is nicer
            'include_html': True,
        },
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
            'formatter': 'simple'
        },
        # Log to a text file that can be rotated by logrotate
        'logfile': {
            'level':'WARN',
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': os.path.join(SITE_ROOT, 'log').replace('\\', '/') + '/error.log',
            'formatter': 'simple'
        },
    },
    'loggers': {
        # Again, default Django configuration to email unhandled exceptions
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        # Might as well log any errors anywhere else in Django
        'django': {
            'handlers': ['logfile'],
            'level': 'ERROR',
            'propagate': False,
        },
        # Your own app - this assumes all your logger names start with "myapp."
        'doorfy': {
            'handlers': ['logfile', 'console'],
            'level': 'DEBUG', # Or maybe INFO or DEBUG
            'propogate': False
        },
    },
}

# 验证码显示顺序
CAPTCHA_OUTPUT_FORMAT = u'%(hidden_field)s %(text_field)s %(image)s '
# 验证码噪声算法
CAPTCHA_NOISE_FUNCTIONS = ('captcha.helpers.noise_dots',)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.request",
    "doorfy_server.account.context_processors.base",
)

# Close the session when user closes the browser
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

# 过期时间定为1个月
SESSION_COOKIE_AGE = 60 * 60 * 24 * 30

AUTH_PROFILE_MODULE = 'account.UserProfile'

#附件上传配置项
FILE_UPLOAD_PATH = os.path.join(SITE_ROOT, 'static/attach/').replace('\\', '/')
FILE_UPLOAD_HANDLERS = (
    "django.core.files.uploadhandler.MemoryFileUploadHandler",
    "django.core.files.uploadhandler.TemporaryFileUploadHandler",
)
DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
# for user upload
ALLOW_FILE_TYPES = ('.jpg', '.jpeg', '.gif', '.bmp', '.png', '.rar', '.zip')

LOGIN_URL = '/account/login/'

#邮件配置项
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'noreply@doorfy.com'
EMAIL_USE_TLS = True
EMAIL_HOST_PASSWORD = ''
DEFAULT_FROM_EMAIL = 'noreply@doorfy.com'
SERVER_EMAIL = 'noreply@doorfy.com'
# 调试邮件
DEBUG_EMAIL = 'hello@me.com'

SITE_DOMAIN = "127.0.0.1:8000"

COMPRESS_CSS_FILTERS = ['compressor.filters.css_default.CssAbsoluteFilter','compressor.filters.yui.YUICSSFilter']
COMPRESS_JS_FILTERS = ['compressor.filters.yui.YUIJSFilter']
COMPRESS_YUI_BINARY = 'java -jar ' + SITE_ROOT + "/util/yuicompressor-2.4.7.jar"
COMPRESS_ENABLED = True
COMPRESS_URL = '/style/'

CLOUD_HOST = ""
CLOUD_ACCESS_ID = ""
CLOUD_SECRET_ACCESS_KEY = ""
CLOUD_BUCKET = ''

try:
    from settings_deploy import *
    pass
except ImportError:
    pass
