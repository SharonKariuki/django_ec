from django.shortcuts import render, redirect
from .models import Product, Category
from .forms import ProductForm, CategoryForm

# Home page view
def home(request):
    return render(request, "products/home.html")


# Add a new category
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("products:category_list")  # redirect to category list after adding
    else:
        form = CategoryForm()
    return render(request, "products/category_form.html", {'form': form})


# List all categories
def category_list(request):
    categories = Category.objects.all()
    return render(request, "products/category_list.html", {'categories': categories})


# Add a new product
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('products:list_products')  # redirect to product list
    else:
        form = ProductForm()
    return render(request, 'products/add_product.html', {'form': form})


# List all products
def list_products(request):
    products = Product.objects.all()
    return render(request, 'products/list_products.html', {'products': products})
