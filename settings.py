# Django settings for experimentdb project.

import os.path
PROJECT_DIR = os.path.dirname(__file__)
STATIC_DOC_ROOT = os.path.join(PROJECT_DIR, "static")

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

try:
    from localsettings import *
except ImportError:
    print 'localsetting could not be imported'
    pass #Or raise

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(PROJECT_DIR, "media/files")

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/static/admin-media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'ci%^08ig-0qu*&b(kz_=n6lvbx*puyx6=8!yxzm0+*z)w@7+%6'

LOGIN_URL = '/experimentdb/accounts/login/'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware'
)

TEMPLATE_CONTEXT_PROCESSORS  = (
	'django.contrib.auth.context_processors.auth',
	'django.contrib.messages.context_processors.messages',
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
    'experimentdb.projects',
    'experimentdb.proteins',
    'experimentdb.reagents',
    'experimentdb.external',
    'experimentdb.cloning',
    'experimentdb.datasets',
    'experimentdb.sharing',
    'experimentdb.data',
    'experimentdb.hypotheses',
    'ajax_select',
    'south'
)


AJAX_LOOKUP_CHANNELS = {
	'antibody' : ('experimentdb.reagents.lookups', 'AntibodyLookup'),
	'construct' : ('experimentdb.reagents.lookups', 'ConstructLookup'),
	'chemical' : ('experimentdb.reagents.lookups', 'ChemicalLookup'),
	'siRNA' : ('experimentdb.reagents.lookups', 'SiRNALookup'),
	'strain' : ('experimentdb.reagents.lookups', 'StrainLookup'),
	'cell' : ('experimentdb.reagents.lookups', 'CellLineLookup'),	
	'protein' : ('experimentdb.proteins.lookups', 'ProteinLookup'),		
	'protocol' : ('experimentdb.data.lookups', 'ProtocolLookup'),		
	}
