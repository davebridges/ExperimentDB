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
MEDIA_ROOT = os.path.join(PROJECT_DIR, "media/files") #set to where pictures and files will be stored.  Default is media folder and this is where MEDIA_URL on your webserver should point
STATIC_ROOT = os.path.join(PROJECT_DIR, "served-static") #this folder is populated by the collectstatic command and is where STATIC_URL on your webserver should point

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
        'NAME': 'default.db' # Or path to database file if using sqlite3.
        'ENGINE': 'django.db.backends.sqlite3', #  Choose one of 'django.db.backends.postgresql_psycopg2','django.db.backends.postgresql', 'django.db.backends.mysql', 'django.db.backends.sqlite3', 'django.db.backends.oracle'
        'USER': '',  # Not used with sqlite3.
        'PASSWORD': '', # Not used with sqlite3
	'HOST':'', # Set to empty string for localhost. Not used with sqlite3.
	'PORT':'', # Set to empty string for default. Not used with sqlite3.
    }
}
