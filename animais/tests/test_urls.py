from django.test import TestCase, RequestFactory
from django.urls import reverse
from animais.views import index


class AnimaisUrlsTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def test_rota_url_utiliza_view_index(self):
        """Teste da home da aplicação utiliza a view da aplicaçao"""
        request = self.factory.get('/')
        response = index(request)
        self.assertEqual(response.status_code, 200)