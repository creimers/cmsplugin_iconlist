# -*- coding: utf-8 -*-

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.contrib import admin

from .models import IconList
from .models import Icon



class ChoiceInline(admin.TabularInline):
    model = Icon
    extra = 1


class IconListPlugin(CMSPluginBase):
    name = u'Icon List'
    model = IconList
    render_template = "cmsplugin_iconlist/_iconlist_plugin.html"
    inlines = [ChoiceInline, ]

    def render(self, context, instance, placeholder):
        items = instance.associated_item.all()
        context.update({
            'items': items,
            'instance': instance,
        })
        return context

plugin_pool.register_plugin(IconListPlugin)
