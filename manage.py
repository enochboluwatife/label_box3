#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'labelbox_webapp.settings')

    # Check for the PORT environment variable (defaults to 8000 if not set)
    port = os.environ.get("PORT", "8000")

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # Run the server, binding to all IPs (0.0.0.0) and using the correct port
    execute_from_command_line([sys.argv[0], "runserver", f"0.0.0.0:{port}"])

if __name__ == '__main__':
    main()
