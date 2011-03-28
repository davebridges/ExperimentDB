import os
import sys

path = 'C:\Documents and Settings\davebrid\My Documents\SRC'

if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'experimentdb.settings'


import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

