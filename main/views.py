from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group  # Dodano
from .forms import UserCreationWithGroupForm  

## Create your views here.
@login_required
def homepage(request):

    if request.user.groups.filter(name='Korisnik').exists():
        print("User is part of the Korisnik group.")
        return render(request, 'main/user_homepage.html')
    else: 
        print('user is admin')
        return render(request, 'main/admin_homepage.html')


    #return render(request, 'main/homepage.html')    # DJANGO automatski trazi html datoteku pod templates folder, zbog postavke u settingsima APP_DIRS = True, svaka app ce imati svoj templates folder
    #return HttpResponse('Welcome to our homepage! <strong>#samoKAFICH</strong>')    



 

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)  
        if form.is_valid():  
            user = form.save()  

            group = Group.objects.get(name='Korisnik')  
            group.user_set.add(user)  


            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password) 
            login(request, user) 
            return redirect('main:homepage') 
    else:
        form = UserCreationForm()  

    context = {'form': form}
    return render(request, 'registration/register.html', context)



@login_required
def manage_users(request):
    if request.user.groups.filter(name='Korisnik').exists():
        return redirect('main:homepage')  

    users = User.objects.all()  
    return render(request, 'main/manage_users.html', {'users': users})




@login_required
def edit_user(request, user_id):
    if request.user.groups.filter(name='Korisnik').exists():
        return redirect('main:homepage')

    user = User.objects.get(id=user_id)
    if request.method == 'POST':
        user.username = request.POST.get('username', user.username)
        user.email = request.POST.get('email', user.email)
        user.save()
        return redirect('main:manage_users')

    return render(request, 'main/edit_user.html', {'user': user})

@login_required
def delete_user(request, user_id):
    if request.user.groups.filter(name='Korisnik').exists():
        return redirect('main:homepage')

    user = User.objects.get(id=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('main:manage_users')

    return render(request, 'main/delete_user.html', {'user': user})




@login_required
def add_user(request):
    if not request.user.groups.filter(name='Korisnik').exists():  
        if request.method == 'POST':
            form = UserCreationWithGroupForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('main:manage_users') 
        else:
            form = UserCreationWithGroupForm()  

        return render(request, 'main/add_user.html', {'form': form}) 
    else:
        return redirect('main:homepage') 


@login_required
def show_other_users(request):
   
    if request.user.groups.filter(name='Korisnik').exists() and not request.user.is_superuser:
        
        users = User.objects.exclude(id=request.user.id)
        return render(request, 'main/show_other_users.html', {'users': users})
    else:
       
        return redirect('main:manage_users')