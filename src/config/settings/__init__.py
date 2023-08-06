from split_settings.tools import include as settings_include
from split_settings.tools import optional

settings_include(
    'django.py',
    optional('local_settings.py'),
)
