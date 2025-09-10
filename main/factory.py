import factory
from factory.django import DjangoModelFactory

from main.models import *

class PiceFactory(DjangoModelFactory):
    class Meta:
        model = Pice

    pice_naziv = factory.Faker('word')
    pice_opis = factory.Faker('sentence')
    pice_kolicina_u_ml = factory.Faker('random_number', digits=3)
    pice_sadrzi_alkohol = factory.Faker('boolean')
    pice_vegansko = factory.Faker('boolean')
    pice_poj_cijena = factory.Faker('pydecimal', left_digits=2, right_digits=2, positive=True)