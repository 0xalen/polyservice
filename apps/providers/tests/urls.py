from django.test import SimpleTestCase
from django.urls import reverse, resolve
from apps.providers import views
from apps.providers.tests.data import TestProvidersUrlsBase


class TestProvidersUrls(TestProvidersUrlsBase):
    """
    Class for testing providers app urls.
    Run:
        python manage.py test apps.providers.tests.urls.TestProvidersUrls --keepdb
    """

    def test_url_get_provider_information_resolves_to_view(self):
        url = self.url_get_provider_detail
        self.assertEqual(resolve(url).func.view_class, views.ProviderInformationView)

    def test_url_update_provider_information_resolves_to_view(self):
        url = self.url_update_provider_information
        self.assertEqual(resolve(url).func.view_class, views.ProviderInformationView)

    def test_url_delete_provider_resolves_to_view(self):
        url = self.url_delete_provider
        self.assertEqual(resolve(url).func.view_class, views.ProviderInformationView)

    def test_url_create_provider_resolves_to_view(self):
        url = self.url_create_provider
        self.assertEqual(resolve(url).func.view_class, views.ProviderInformationView)

    def test_url_get_provider_list_resolves_to_view(self):
        url = self.url_get_provider_list
        self.assertEqual(resolve(url).func.view_class, views.ProviderListView)
