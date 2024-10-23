"""
WSGI config for MyProject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

from MyProject import wsgi
import sys
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MyProject.settings')

application = get_wsgi_application()

path = 'EliteTravel/Myproject'
if path not in sys.path:
    sys.path.append(path)

application = wsgi.application
