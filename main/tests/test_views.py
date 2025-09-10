from django.test import TestCase, Client
from django.urls import reverse
from main.models import Pice, Narudzba, User


class TestViews(TestCase):

    def setUp(self):
        self.client = Client() 
        self.drink_list_url = reverse('main:drink_list_view')

       
        self.pice1 = Pice.objects.create(
            pice_naziv="Coca-Cola",
            pice_opis="Gazirano piće",
            pice_kolicina_u_ml=500,
            pice_sadrzi_alkohol=False,
            pice_vegansko=True,
            pice_poj_cijena=2.50
        )

    def test_pice_list_view_GET(self):
        """Test za get request prikaza liste pića"""
        response = self.client.get(self.drink_list_url)

        self.assertEqual(response.status_code, 200) 
        self.assertTemplateUsed(response, 'main/admin/lista_pica/list_view.html') 
        self.assertContains(response, "Coca-Cola") 

        
