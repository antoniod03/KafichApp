# Generated by Django 5.1.1 on 2024-12-16 18:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_konobar_konobar_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='narudzba',
            name='narudzba_kolicina_stavki',
            field=models.PositiveIntegerField(blank=True, validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]