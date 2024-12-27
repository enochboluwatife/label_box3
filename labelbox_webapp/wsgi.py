"""
WSGI config for labelbox_webapp project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'labelbox_webapp.settings')

application = get_wsgi_application()

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'labelbox_webapp.settings')
    port = os.environ.get("PORT", "8000")  # Default to port 8000 if PORT is not set
    execute_from_command_line(["manage.py", "runserver", f"0.0.0.0:{port}"])
