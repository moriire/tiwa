import os
from dotenv import load_dotenv
load_dotenv()
get = os.getenv

DJANGO_SETTINGS_MODULE = 'backend.settings.dev_settings' if get("APP_MODE")=="dev" else 'backend.settings.prod_settings'
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', DJANGO_SETTINGS_MODULE)

application = get_wsgi_application()
