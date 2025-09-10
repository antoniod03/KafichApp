import random

from django.db import transaction
from django.core.management.base import BaseCommand
from main.models import Pice
from main.factory import PiceFactory

NUM_PICE = 10  # Number of Pice instances to create
class Command(BaseCommand):
    help = 'postavlja testne podatke u bazu podataka'

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write('brisanje starih podataka...')
        Pice.objects.all().delete()
        self.stdout.write('postavljanje testnih podataka...')
        
        for _ in range(NUM_PICE):
            PiceFactory()
