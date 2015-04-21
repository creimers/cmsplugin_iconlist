[![Build Status](https://travis-ci.org/creimers/cmsplugin_iconlist.svg?branch=develop)](https://travis-ci.org/creimers/cmsplugin_iconlist)
[![Coverage Status](https://coveralls.io/repos/creimers/cmsplugin_iconlist/badge.svg?branch=develop)](https://coveralls.io/r/creimers/cmsplugin_iconlist?branch=develop)
[![Latest Version](https://pypip.in/version/cmsplugin_iconlist/badge.svg)](https://pypi.python.org/pypi/cmsplugin-iconlist/)
[![Supported Python versions](https://pypip.in/py_versions/cmsplugin_iconlist/badge.svg)](https://pypi.python.org/pypi/cmsplugin-iconlist/)
[![Development Status](https://pypip.in/status/cmsplugin_iconlist/badge.svg)](https://pypi.python.org/pypi/cmsplugin_iconlist/)
[![Code Climate](https://codeclimate.com/github/creimers/cmsplugin_iconlist/badges/gpa.svg)](https://codeclimate.com/github/creimers/cmsplugin_iconlist)
# djangocms icon list plugin

A djangocms plugin displaying font-awesome icons in a list, like so:

![preview](preview.png)

## Installation

* ``pip install cmsplugin_iconlist``

* add ``'cmsplugin_iconlist'`` to ``INSTALLED_APPS`` in ``settings.py``

if you're using Django >= 1.7:

* add ``'cmsplugin_iconlist': 'cmsplugin_iconlist.migrations_django'`` to ``MIGRATION_MODULES`` in ``settings.py``

* migrate the database

## Customize avaliable icons

In case you need other icons than the defaults, add the ``ICON_LIST`` variable to settings like so:

```
ICON_CHOICES = (
    ('fa-facebook', 'facebook'),
    ('fa-foursquare', 'foursquare'),
    ('...', '...'),
)
```

A full list of available icons can be found [here](http://fontawesome.io/icons/).
