# Django settings for experimentdb project.

import os.path
PROJECT_DIR = os.path.dirname(__file__)
STATIC_DOC_ROOT = os.path.join(PROJECT_DIR, "static")
STATICFILES_DIRS = (os.path.join(PROJECT_DIR, "static"),
)

DEBUG = True
TEMPLATE_DEBUG = DEBUG

try:
    from localsettings import *
except ImportError:
    from localsettings_defualt import *
    print 'localsetting could not be imported'

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
