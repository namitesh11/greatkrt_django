from store.models import product
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    products=product.objects.all().filter(is_avilable=True)
    
    context={
        'products':products,
    }
    
    return render(request ,'home.html',context)