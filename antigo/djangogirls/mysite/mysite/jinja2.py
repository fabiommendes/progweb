from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse

from jinja2 import Environment


def environment(**options):
    env = Environment(**options)
    env.globals.update({
        'static': staticfiles_storage.url,
        'url': reverse,
        'the_answer': lambda: 42,
    })
    env.filters.update({
        'UPPER': lambda x: x.upper(),
        'plus': lambda x, y: x + y,
        
    })
    return env