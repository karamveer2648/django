from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.

from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def recipes(request):
    if request.method == 'POST':
        data = request.POST
        recipe.objects.create(
            user = request.user,
            name=data.get('name'),
            ingredients=data.get('ingredients'),
            prep_time=data.get('prep_time'),
            prep_guide=data.get('prep_guide'),
            image=request.FILES.get('image'),
            category=data.get('category'),
            date_created=data.get('date_created'),
        )
        messages.success(request, "Recipe added successfully")
        return redirect('/Add_Recipe/')
    return render(request, 'Add_Recipe.html')

@login_required(login_url='/login/')
def listrecipes(request):
    queryset = recipe.objects.all()  # Correct model capitalization
    

    if request.GET.get('q'):
       print(request.GET.get('q'))
       queryset = recipe.objects.filter(name__icontains=request.GET.get('q'))
    return render(request,'Recipes.html',context = {'recipes': queryset}) 

# Function to render the template
def listingrecipes(request):
    response = listrecipes(request)  # Call listrecipes() to get response
    return response  # Directly return the response

@login_required(login_url='/login/')
def delete_recipe(request, id):
    queryset = recipe.objects.get(id=id)
    if request.user != queryset.user:
        messages.error(request, "You are not allowed to delete this recipe")
        return redirect('/list/')
    else:
        queryset.delete()
        return redirect('/list/')

@login_required(login_url='/login/')
def view_recipe(request, id):
    queryset = recipe.objects.get(id=id)
    context = {'recipe':queryset}
    return render(request, 'view_recipe.html', context)


@login_required(login_url='/login/')
def update_recipe(request, id):
    queryset = recipe.objects.get(id=id)
    if request.user != queryset.user:
        messages.error(request, "You are not allowed to edit this recipe")
        return redirect('/list/')
    else:

        if request.method == 'POST':
            name = request.POST.get('name')
            ingredients = request.POST.get('ingredients')
            prep_time = request.POST.get('prep_time')
            prep_guide = request.POST.get('prep_guide')
            image = request.FILES.get('image')
            category = request.POST.get('category')
            date_created = request.POST.get('date_created')

            queryset.name = name
            queryset.ingredients = ingredients
            queryset.prep_time = prep_time
            queryset.prep_guide = prep_guide
            queryset.image = image
            queryset.category = category
            queryset.date_created = date_created
            queryset.save()
            return redirect('/list/')  
        
        context = {'recipe':queryset}
    return render(request, 'update_recipe.html', context)

def login_page(request):
    
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        
        user = User.objects.filter(username=username)
        if not user.exists():
            messages.error(request, "Invalid Username")
            return redirect('/login/')
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('/list/')
        else:
            messages.error(request, "Invalid Password")
            return redirect('/login/')
        
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('/register/')
        
        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            username=username
        )
        user.set_password(password)
        user.save()
        messages.success(request, "Account created successfully")
        return redirect('/login/')  
        
    return render(request, 'register.html')


def logout_user(request):
    logout(request)
    return redirect('/home/')
