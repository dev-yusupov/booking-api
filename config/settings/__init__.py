ENV_NAME = 'Local'

from config.settings.base import *
import os


if ENV_NAME == 'Production':
    from config.settings.production import *
else:
    from config.settings.local import *