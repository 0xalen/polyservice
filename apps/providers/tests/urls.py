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

    def test_url_url_provider_detail_resolves_to_view(self):
        url = self.url_provider_detail
        self.assertEqual(resolve(url).func.view_class, views.ProviderInformationView)

    def test_url_provider_update_information_resolves_to_view(self):
        url = self.url_provider_update
        self.assertEqual(resolve(url).func.view_class, views.ProviderInformationView)

    def test_url_delete_provider_resolves_to_view(self):
        url = self.url_provider_delete
        self.assertEqual(resolve(url).func.view_class, views.ProviderInformationView)

    def test_url_create_provider_resolves_to_view(self):
        url = self.url_provider_create
        self.assertEqual(resolve(url).func.view_class, views.ProviderInformationView)

    def test_url_get_provider_list_resolves_to_view(self):
        url = self.url_provider_list
        self.assertEqual(resolve(url).func.view_class, views.ProviderListView)
