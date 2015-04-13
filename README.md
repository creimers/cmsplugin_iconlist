[![Latest Version](https://pypip.in/version/cmsplugin_iconlist/badge.svg)](https://pypi.python.org/pypi/cmsplugin-iconlist/)
[![Supported Python versions](https://pypip.in/py_versions/cmsplugin_iconlist/badge.svg)](https://pypi.python.org/pypi/cmsplugin-iconlist/)
[![Development Status](https://pypip.in/status/cmsplugin_iconlist/badge.svg)](https://pypi.python.org/pypi/cmsplugin_iconlist/)
# djangocms icon list plugin

A djangocms plugin displaying font-awesome icons in a list

## Installation

* ``pip install cmsplugin_iconlist``

* add ``cmsplugin_iconlist`` to ``INSTALLED_APPS`` in ``settings.py``

if you're using Django >= 1.7:

* add ``'cmsplugin_iconlist': 'cmsplugin_instagram.migrations_django'`` to ``MIGRATION_MODULES`` in ``settings.py``

* migrate the database

## Customize avaliable icons

In case you need other icons than the defaults, add ``ICON_LIST`` variable to settings like so:

```
ICON_CHOICES = (
    ('fa-facebook', 'facebook'),
    ('fa-foursquare', 'foursquare'),
    ('...', '...'),
)
```

A full list of available icons can be found [here](http://fontawesome.io/icons/).
