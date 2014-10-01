# -*- coding: utf-8 -*-
"""Generate datetime UTC - RFC 3339 formatting in Python"""

__author__ = "Gonzalo Chacaltana"

# first -> pip install rfc3339

import datetime
import rfc3339

print rfc3339.rfc3339(datetime.datetime.utcnow())
