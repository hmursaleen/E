from django.urls import path

from . import views

urlpatterns = [
	path('<int:pk>/', views.vendor_detail, name='vendor_detail')
]