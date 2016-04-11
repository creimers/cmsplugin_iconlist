[![Build Status](https://travis-ci.org/creimers/cmsplugin_iconlist.svg?branch=develop)](https://travis-ci.org/creimers/cmsplugin_iconlist)
[![Coverage Status](https://coveralls.io/repos/creimers/cmsplugin_iconlist/badge.svg?branch=develop)](https://coveralls.io/r/creimers/cmsplugin_iconlist?branch=develop)
[![Latest Version](https://img.shields.io/pypi/v/cmsplugin_iconlist.svg)](https://pypi.python.org/pypi/cmsplugin_iconlist)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/cmsplugin_iconlist.svg)](https://pypi.python.org/pypi/cmsplugin_iconlist)
[![Status](https://img.shields.io/pypi/status/cmsplugin_iconlist.svg)](https://pypi.python.org/pypi/cmsplugin_iconlist)
[![Code Climate](https://codeclimate.com/github/creimers/cmsplugin_iconlist/badges/gpa.svg)](https://codeclimate.com/github/creimers/cmsplugin_iconlist)
[![Requirements Status](https://requires.io/github/creimers/cmsplugin_iconlist/requirements.svg?branch=develop)](https://requires.io/github/creimers/cmsplugin_iconlist/requirements/?branch=develop)
# djangocms icon list plugin

A djangocms plugin displaying font-awesome icons in a list, like so for example:

![preview](preview.png)

Works with django 1.7 and 1.8, works with djangocms 3.0 and 3.1.

Should also work with Django 1.9 and djangoCMS 3.2, but that has not been tested.

## Installation

* ``pip install cmsplugin_iconlist``

* add ``'cmsplugin_iconlist'`` to ``INSTALLED_APPS`` in ``settings.py``

if you're using Django < 1.7:

* migrations are in ``migrations_south``.

* migrate the database

## Customize avaliable icons

In case you need other icons than the defaults, add the ``ICON_CHOICES`` variable to ``settings.py`` like so:

```
ICON_CHOICES = (
    ('fa-facebook', 'facebook'),
    ('fa-foursquare', 'foursquare'),
    ('...', '...'),
)
```

A full list of available icons can be found at [fontawesome](http://fontawesome.io/icons/).
