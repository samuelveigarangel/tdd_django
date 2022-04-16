from django.test import TestCase, RequestFactory
from animais.models import Animal

class animalModelTestCase(TestCase):

    def setUp(self):
        self.animal = Animal.objects.create(
            nome_animal='leão',
            predador='Sim',
            venenoso='Não',
            domestico='Não'
        )

    def test_animal_cadastrado_caracteristicas(self):
        """Teste que verifica sem o animal está cadastrado com suas respectivas caracteristicas"""
        self.assertEqual(self.Animal.nome_animal, 'leão')