# -*- coding: utf-8 -*-

"""
WSGI config for ecoloscore project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
import sys
import site

ecoloscore_home = '~ecoloscore'

site.addsitedir(os.path.join(
    ecoloscore_home,
    'venv_ecoloscore/local/lib/python2.7/site-packages'))

sys.path.append('~ecoloscore/www')
sys.path.append('~ecoloscore/www/ecoloscore')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ecoloscore.settings")

activate_env = os.path.expanduser(os.path.join(
    ecoloscore_home,
    'venv_ecoloscore/bin/activate_this.py'))
execfile(activate_env, dict(__file__=activate_env))

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
