from django.test import SimpleTestCase
from django.urls import reverse, resolve
from main.views import (
    homepage, manage_users, register, register_superuser, edit_user, delete_user, add_user,
    add_admin, add_konobar, show_other_users, dodaj_pice, kreiraj_narudzbu,
    PiceListView, PiceDetailView, NarudzbaListView, NarudzbaDetailView, 
    StavkaNarudzbeDetailView, KonobarDetailView
)


class TestUrls(SimpleTestCase):

    def test_homepage_url_is_resolved(self):
        url = reverse('main:homepage')
        self.assertEqual(resolve(url).func, homepage)

    def test_manage_users_url_is_resolved(self):
        url = reverse('main:manage_users')
        self.assertEqual(resolve(url).func, manage_users)

    def test_register_url_is_resolved(self):
        url = reverse('main:register')
        self.assertEqual(resolve(url).func, register)

    def test_register_superuser_url_is_resolved(self):
        url = reverse('main:register_superuser')
        self.assertEqual(resolve(url).func, register_superuser)

    def test_pice_list_view_url_is_resolved(self):
        url = reverse('main:drink_list_view')
        self.assertEqual(resolve(url).func.view_class, PiceListView)


