from django.test import TestCase, RequestFactory
from animais.models import animal

class animalModelTestCase(TestCase):

    def setUp(self):
        self.animal = animal.objects.create(
            nome_animal='Leão',
            predador='Sim',
            venenoso='Não',
            domestico='Não'
        )

    def test_animal_cadastrado_caracteristicas(self):
        """Teste que verifica sem o animal está cadastrado com suas respectivas caracteristicas"""
        self.assertEqual(self.animal.nome_animal, 'Leão')