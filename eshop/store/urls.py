from django.urls import path
from . import views

urlpatterns = [
	path('search/', views.search, name='search'),
	path('product/<slug:slug>/', views.category_detail, name='category_detail'),
	path('product/<slug:category_slug>/<slug:slug>/', views.product_detail, name='product_detail'),
] 