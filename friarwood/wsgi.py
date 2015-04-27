"""
WSGI config for friarwood project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import sys
from imp import reload 

reload(sys)     
sys.setdefaultencoding("utf-8")

import os

#Heroku
from django.core.wsgi import get_wsgi_application
from dj_static import Cling

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "friarwood.settings")

#application = get_wsgi_application()

#Heroku
application = Cling(get_wsgi_application())
