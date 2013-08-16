import os
import sys

sys.path.append('/var/www/internal/ExperimentDB/')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "experimentdb.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
