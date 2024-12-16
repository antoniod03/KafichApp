from django import forms
from django.contrib.auth.models import User, Group

from .models import *




class KonobarCreationForm(forms.ModelForm):

    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)    # required dal treba?
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

    konobar_ime = forms.CharField(label="First Name", required=True)
    konobar_prezime = forms.CharField(label="Last Name", required=True)
    konobar_telefon = forms.CharField(label="Phone", required=False)

    class Meta:
        model = User
        fields = ['username', 'email']


    def clean_password2(self):

        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):

        user = super(KonobarCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])  
            
        if commit:
            user.save()

        group = Group.objects.get(name='Korisnik')
        group.user_set.add(user)


        konobar = Konobar.objects.create(
            user=user,  
            konobar_ime=self.cleaned_data.get("konobar_ime"),
            konobar_prezime=self.cleaned_data.get("konobar_prezime"),
            konobar_telefon=self.cleaned_data.get("konobar_telefon"),
        )

        return user  


class AdminCreationForm(forms.ModelForm):

    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email']  

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super(AdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])  
        
        if commit:
            user.save()

       
        group = Group.objects.get(name='Administrator')  
        group.user_set.add(user)  

        return user



class PiceForm(forms.ModelForm):
    class Meta:
        model = Pice
        fields = ['pice_naziv', 'pice_opis', 'pice_kolicina_u_ml', 'pice_sadrzi_alkohol', 'pice_vegansko', 'pice_poj_cijena']

    pice_naziv = forms.CharField(required=True)
    pice_kolicina_u_ml = forms.IntegerField(required=True)



class NarudzbaForm(forms.ModelForm):
    class Meta:
        model = Narudzba
        fields = ['narudzba_kolicina_stavki', 'narudzba_placena']
        widgets = {
            'narudzba_kolicina_stavki': forms.HiddenInput()  
        }



class StavkaNarudzbeForm(forms.ModelForm):
    class Meta:
        model = StavkaNarudzbe
        fields = ['stavka_pice', 'stavka_kolicina_pica']




"""
class UserCreationWithGroupForm(forms.ModelForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)
    
    group = forms.ModelChoiceField(queryset=Group.objects.all(), required=True, label="Role")

    konobar_ime = forms.CharField(label="First Name", required=True)
    konobar_prezime = forms.CharField(label="Last Name", required=True)
    konobar_telefon = forms.CharField(label="Phone", required=False)


    class Meta:
        model = User
        fields = ['username', 'email']  

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        
        # Dodavanje korisnika u odabranu grupu
        group = self.cleaned_data.get("group")
        group.user_set.add(user)


        if group.name == 'Konobar':
            Konobar.objects.create(
                user = user,
                konobar_ime = self.cleaned_data.get("konobar_ime"),
                konobar_prezime = self.cleaned_data.get("konobar_prezime"),
                konobar_telefon = self.cleaned_data.get("konobar_telefon"),
            )

        return user

"""

