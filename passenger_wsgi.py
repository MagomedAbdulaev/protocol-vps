import os, sys
sys.path.insert(0, '/home/m/magomed487/protocol-vps.magomed487.beget.tech/protocol')
sys.path.insert(1, '/home/m/magomed487/protocol-vps.magomed487.beget.tech/venv_django/lib/python3.11/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'protocol.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()