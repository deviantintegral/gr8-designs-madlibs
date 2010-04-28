import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'gr8girls.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
  sys.path.append('/var/www/django-sites')

