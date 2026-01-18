"""
ASGI config for cinema_service project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
<<<<<<< HEAD
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
=======
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
>>>>>>> 1f225beee00415b859782acdae7cb6ded83764f9
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cinema_service.settings")

application = get_asgi_application()
