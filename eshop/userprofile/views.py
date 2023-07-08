from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.text import slugify
from . models import Userprofile
# Create your views here.

from store.forms import ProductForm

def vendor_detail(request, pk):
	user = User.objects.get(pk=pk)

	return render(request, 'userprofile/vendor_detail.html', {
		'user' : user,
		})

@login_required
def mystore(request):
	return render(request, 'userprofile/mystore.html')


@login_required
def add_product(request):
	if request.method == 'POST':
		form = ProductForm(request.POST, request.FILES)

		if form.is_valid():
			title = request.POST.get('title')
			product = form.save(commit=False)
			product.user = request.user 
			product.slug = slugify(title)
			product.save()

			return redirect('mystore')

	else:
		form = ProductForm()

	return render(request, 'userprofile/add_product.html', {
		'form' : form,
		})


@login_required
def myaccount(request):
	return render(request, 'userprofile/myaccount.html')


def signup(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)

		if form.is_valid():
			user = form.save()
			login(request, user)
			userprofile = Userprofile.objects.create(user=user)
			return redirect('frontpage')

	else:
		form = UserCreationForm()

	return render(request, 'userprofile/signup.html', {
		'form' : form, 
		})