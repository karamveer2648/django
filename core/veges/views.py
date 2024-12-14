from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from django.shortcuts import render

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

def delete_recipe(request, id):
    print(id)
    queryset = recipe.objects.get(id=id)
    queryset.delete()
    return redirect('/list/')

def update_recipe(request, id):
    queryset = recipe.objects.get(id=id)

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



