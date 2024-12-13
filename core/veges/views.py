from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def recipes(request):
    if request.method == 'POST':
        data = request.POST
        recipe.objects.create(
                name = data.get('name'), 
                ingredients = data.get('ingredients'), 
                prep_time = data.get('prep_time'), 
                prep_guide= data.get('prep_guide'), 
                image = request.FILES.get('image'), 
                category = data.get('category'), 
                date_created = data.get('date_created'),
        )
        return redirect('/Add_Recipe/')
    return render(request, 'Add_Recipe.html')
def listrecipes():
    queryset = recipe.objects.all()  # Correct model capitalization
    context = {'recipes': queryset}
    return context 

# Function to render the template
def listingrecipes(request):
    context = listrecipes()  # Call listrecipes() to get context
    return render(request, 'Recipes.html', context)



