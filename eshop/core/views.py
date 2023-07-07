from django.shortcuts import render

# Create your views here.
from store.models import Product
#i want to show all newest products, so i've to import this 

def frontpage(request):
	products = Product.objects.all()[0:6] #want to show first six products
	return render(request, 'core/frontpage.html', {
		'products' : products,
		})

def about(request):
	return render(request, 'core/about.html')