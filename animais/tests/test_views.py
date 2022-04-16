from django.test import TestCase, RequestFactory
from django.db.models.query import QuerySet
from animais.models import animal


class indexViewTestCase(TestCase):

    def setUp(self):
        self.animal = animal.objects.create(
            nome_animal='Gato',
            predador='Não',
            venenoso='Não',
            domestico='Sim'
        )
        self.factory = RequestFactory()

    def test_index_views_retorna_caracteristicas(self):
        """Verifica se a index retorna as caracteristicas do animal do pesquisado"""

        response = self.client.get('/', {'buscar': 'Gato'})
        caracteristica_animal_pesquisado = response.context['caracteristicas']
        self.assertIs(type(response.context['caracteristicas']), QuerySet)
        self.assertEqual(caracteristica_animal_pesquisado[0].nome_animal, 'Gato')
