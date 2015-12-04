# -*- coding: utf-8 -*-

LOGIN = '*****'

PASSWD = '*****'

API = {
    'URL': 'http://domain.tld/',
    'LOGIN_ROUTE': 'ecoauth/login/',
    'PROFILES_ROUTE': 'users/profiles/',
    'CHECKS_ROUTE': 'checkpoints/checks/',
    'TAKES_ROUTE': 'coffeecups/takes/',
    'THROWS_ROUTE': 'coffeecups/throws/'
}

TAG_REGEX = "^ID: ([0-9]*) - TAG: ([0-9A-F]{2}) ([0-9A-F]{2}) ([0-9A-F]{2}) ([0-9A-F]{2})"

DEVICE = '/dev/ttyUSB0'

ARDUINOS = {
    'stairs': [1, 2],
    'cups': [3],
    'bin': [4],
}

SCREEN = {
    'ENABLED': False,  # You should not set this to True unless you know why
    'URL': 'http://SCREEN.DEVICE.IP/index.php',
}

LOGFILE = '/var/log/ecoloscore.log'
