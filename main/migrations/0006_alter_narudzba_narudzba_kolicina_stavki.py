# Generated by Django 5.1.1 on 2024-12-16 19:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_narudzba_narudzba_kolicina_stavki'),
    ]

    operations = [
        migrations.AlterField(
            model_name='narudzba',
            name='narudzba_kolicina_stavki',
            field=models.PositiveIntegerField(blank=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
