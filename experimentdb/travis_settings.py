# Django settings for experimentdb project.

import os.path
PROJECT_DIR = os.path.dirname(__file__)
STATIC_DOC_ROOT = os.path.join(PROJECT_DIR, "static")
STATICFILES_DIRS = (os.path.join(PROJECT_DIR, "static"),
)

DEBUG = True
TEMPLATE_DEBUG = DEBUG

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1
USE_TZ = True

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = ('django.template.loaders.filesystem.Loader',
 'django.template.loaders.app_directories.Loader')

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'debug_toolbar.middleware.DebugToolbarMiddleware'
)

TEMPLATE_CONTEXT_PROCESSORS  = (
	'django.contrib.auth.context_processors.auth',
	'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.static',
)

ROOT_URLCONF = 'experimentdb.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
	os.path.join(PROJECT_DIR, "templates"),
)

MESSAGE_STORAGE = 'django.contrib.messages.storage.fallback.FallbackStorage'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.comments',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.admindocs',    
    'django.contrib.staticfiles',
    'projects',
    'proteins',
    'reagents',
    'external',
    'cloning',
    'datasets',
    'sharing',
    'data',
    'hypotheses',
    'ajax_select',
    'south',
    'PIL',
	'braces'
)

INTERNAL_IPS = ('127.0.0.1',)

AJAX_LOOKUP_CHANNELS = {
	'antibody' : ('reagents.lookups', 'AntibodyLookup'),
	'construct' : ('reagents.lookups', 'ConstructLookup'),
	'chemical' : ('reagents.lookups', 'ChemicalLookup'),
	'siRNA' : ('reagents.lookups', 'SiRNALookup'),
	'strain' : ('reagents.lookups', 'StrainLookup'),
	'cell' : ('reagents.lookups', 'CellLineLookup'),	
	'protein' : ('proteins.lookups', 'ProteinLookup'),		
	'protocol' : ('data.lookups', 'ProtocolLookup'),		
	}
    
# magically include jqueryUI/js/css
AJAX_SELECT_BOOTSTRAP = True
AJAX_SELECT_INLINES = 'inline'    


ADMINS = (
    ('Your Name', 'email@company.com')
)

MANAGERS = ADMINS

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/' #serve the MEDIA_ROOT to this url
LOGIN_URL = '/accounts/login/'
STATIC_URL = '/static/'

#these locations can be absolue paths or relative to the installation (as is shown here)
MEDIA_ROOT = "/var/www/media/files" #set to where pictures and files will be stored.  Default is media folder and this is where MEDIA_URL on your webserver should point
STATIC_ROOT = "/var/www/served-static" #this folder is populated by the collectstatic command and is where STATIC_URL on your webserver should point

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'ci%^08ig-0qu*&b(kz_=n6lvbx*puyx6=8!yxzm0+*z)w@7+%6'


DEBUG = False
TEMPLATE_DEBUG = DEBUG

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Detroit'

DATABASES = {
    'default': {
        'NAME': 'default.db', # Or path to database file if using sqlite3.
        'ENGINE': 'django.db.backends.sqlite3', #  Choose one of 'django.db.backends.postgresql_psycopg2','django.db.backends.postgresql', 'django.db.backends.mysql', 'django.db.backends.sqlite3', 'django.db.backends.oracle'
        'USER': '',  # Not used with sqlite3.
        'PASSWORD': '', # Not used with sqlite3
	'HOST':'', # Set to empty string for localhost. Not used with sqlite3.
	'PORT':'', # Set to empty string for default. Not used with sqlite3.
    }
}
