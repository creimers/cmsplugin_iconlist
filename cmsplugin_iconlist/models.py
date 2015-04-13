from django.db import models
from django.conf import settings
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from cms.models import CMSPlugin


@python_2_unicode_compatible
class IconList(CMSPlugin):

    name = models.CharField(
        _('name'),
        blank=True,
        null=True,
        default='',
        max_length=32,
    )

    def copy_relations(self, oldinstance):
        for associated_item in oldinstance.associated_item.all():
            associated_item.pk = None
            associated_item.icon_list = self
            associated_item.save()

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Icon(models.Model):

    ICON_CHOICES_DEFAULT = (
        ('fa-facebook', 'facebook'),
        ('fa-foursquare', 'foursquare'),
        ('fa-google-plus', 'google-plus'),
        ('fa-instagram', 'instagram'),
        ('fa-linkedin', 'linkedin'),
        ('fa-twitter', 'twitter'),
        ('fa-xing', 'xing'),
        ('fa-yelp', 'yelp'),
        ('fa-youtube-play', 'youtube'),
    )

    ICON_CHOICES = getattr(settings, 'ICON_CHOICES', ICON_CHOICES_DEFAULT)

    icon_list = models.ForeignKey(
        IconList,
        related_name="associated_item"
    )

    icon = models.CharField(
        _('icon'),
        max_length=200,
        blank=False,
        choices=ICON_CHOICES,
    )

    color = models.CharField(
        _('icon color'),
        max_length=200,
        blank=False,
        default="#000000"
    )

    background_color = models.CharField(
        _('background color'),
        max_length=200,
        blank=False,
        default="#ffffff"
    )

    link = models.URLField(
        _('link'),
        max_length=200,
        blank=False
    )

    def __str__(self):
        return self.icon
