from django.test import TestCase
from main.models import Pice, Konobar, Narudzba, StavkaNarudzbe
from django.contrib.auth.models import User
import uuid


class TestModels(TestCase):

    def setUp(self):

        self.user = User.objects.create(username='testuser')

        self.konobar = Konobar.objects.create(
            user=self.user,
            konobar_ime="Ivan",
            konobar_prezime="Horvat",
            konobar_telefon="0912345678"
        )

        self.pice = Pice.objects.create(
            pice_naziv="Cola",
            pice_opis="Gazirano pice",
            pice_kolicina_u_ml=500,
            pice_sadrzi_alkohol=False,
            pice_vegansko=True,
            pice_poj_cijena=15.00
        )

        self.narudzba = Narudzba.objects.create(
            narudzba_konobar=self.user,
            narudzba_kolicina_stavki=2,
            narudzba_placena=False,
            narudzba_ukupna_cijena=30.00
        )

        self.stavka = StavkaNarudzbe.objects.create(
            stavka_narudzba=self.narudzba,
            stavka_pice=self.pice,
            stavka_kolicina_pica=2
        )

    def test_pice_str_method(self):
        self.assertEqual(str(self.pice), "Cola")
    
    def test_konobar_str_method(self):
        self.assertEqual(str(self.konobar), "Ivan")

    def test_narudzba_total_price_update(self):
        self.narudzba.update_ukupna_cijena()
        self.assertEqual(self.narudzba.narudzba_ukupna_cijena, 30.00)
   
    def test_stavka_narudzbe_total_price(self):
        self.assertEqual(self.stavka.stavka_ukupna_cijena, 30.00)  