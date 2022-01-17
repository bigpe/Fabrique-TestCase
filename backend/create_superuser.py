import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_app.settings")

import django

django.setup()

from django.contrib.auth.models import User
try:
    User.objects.create_superuser('test', 'test@example.com', 'test')
except Exception:
    pass