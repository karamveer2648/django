from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    
    
    
    peoples = [
        {'name':'John','age':25},
        {'name':'Doe','age':30},
        {'name':'Smith','age':35},
        {'name':'Alex','age':40},
        {'name':'Tom','age':45},
        {'name':'Jerry','age':50},
        {'name':'Mickey','age':55},
    ]
    return render(request,"index.html", context={'peoples':peoples})
def about(request):
    return render(request,"about.html")
def contact(request):
    return render(request,"contact.html")