# -*- coding: utf-8 -*-

from datetime import datetime
from conf import LOGFILE


def log(msg):
    with open(LOGFILE, 'a') as logfile:
        logfile.write('{} -- {}\n'.format(str(datetime.now()), msg))
