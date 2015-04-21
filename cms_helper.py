#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
gettext = lambda s: s

HELPER_SETTINGS = {
    'NOSE_ARGS': [
        '-s',
    ],
    'INSTALLED_APPS': [
    ],
    'LANGUAGE_CODE': 'de',
    'LANGUAGES': (
        ('de', gettext('de')),
    ),
    'CMS_LANGUAGES': {
        ## Customize this
        1: [
            {
                'redirect_on_fallback': True,
                'hide_untranslated': False,
                'name': gettext('de'),
                'code': 'de',
                'public': True,
            },
        ],
        'default': {
            'redirect_on_fallback': True,
            'public': True,
            'hide_untranslated': False,
        },
    },
    'MIDDLEWARE_CLASSES': [
        'django.contrib.messages.middleware.MessageMiddleware',
    ],
    'MIGRATION_MODULES': {
        'cms': 'cms.migrations_django',
        'cmsplugin_iconlist': 'cmsplugin_iconlist.migrations_django',
    },
}
