from django.test import TestCase
from django.conf import settings
from django.contrib.auth.models import User

from cms import api
from cms.models import CMSPlugin
from cms.test_utils.testcases import BaseCMSTestCase
from cms.utils import get_cms_setting

from . import models
from . import cms_plugins


class IconListTestCase(TestCase, BaseCMSTestCase):
    su_username = 'user'
    su_password = 'pass'

    def setUp(self):
        self.template = get_cms_setting('TEMPLATES')[0][0]
        self.language = settings.LANGUAGES[0][0]
        self.page = api.create_page('page', self.template, self.language, published=True)
        self.placeholder = self.page.placeholders.all()[0]
        self.superuser = self.create_superuser()

    def tearDown(self):
        self.client.logout()

    def create_superuser(self):
        return User.objects.create_superuser(self.su_username, 'email@example.com', self.su_password)

    def test_add_iconlist_plugin(self):
        iconlist_plugin = api.add_plugin(
            self.placeholder, cms_plugins.IconListPlugin, self.language, name='affe'
        )

        self.assertTrue(models.IconList.objects.filter(pk=iconlist_plugin.pk).exists())
