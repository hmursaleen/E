from django import forms
from . models import Product

class ProductForm(forms.ModelForm):
	class Meta:
		model = Product
		fields = ('category', 'title', 'description', 'price', 'image',)

		widgets = {
		'category' : forms.Select(attrs={
			'class' : 'w-full p-4 border border-gray-200 rounded-xl'
			}),

		'title' : forms.TextInput(attrs={
			'class' : 'w-full p-4 border border-gray-200 rounded-xl'
			}),

		'description' : forms.Textarea(attrs={
			'class' : 'w-full p-4 border border-gray-200 rounded-xl'
			}),

		'price' : forms.TextInput(attrs={
			'class' : 'w-full p-4 border border-gray-200 rounded-xl'
			}),

		'image' : forms.FileInput(attrs={
			'class' : 'w-full p-4 border border-gray-200 rounded-xl'
			}),
		}