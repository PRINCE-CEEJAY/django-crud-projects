from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .form import ProductForm


# Create your views here.
@login_required(login_url='/admin/')
def get_products(request):
    queryset = Product.objects.filter(user=request.user).all().order_by('-date_created')
    context = { 'products': queryset}
    return render(request, 'product/products.html', context)

@login_required(login_url='/admin/')
def search(request):
    # delay just to see transition before request finishes
    import time
    time.sleep(2)
    query = request.GET.get('search')
    product = request.user.product.filter(    
        Q(title__icontains=query) |
        Q(description__icontains=query) |
        Q(price__icontains=query) 
    ) 

    context = {'products': product}
    return render(request, 'product/partials/product-list.html', context)

def create_product(request):
    if request.method == "POST":
        form = ProductForm(data=request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return redirect('get_products')
    return render(request, 'product/partials/add-product.html', {'form': ProductForm()})

@login_required(login_url='/admin/')
def product_detail(request, product_id):
    product = request.user.product.filter(id=product_id).order_by('-date_created')
    context = {'product': product}
    return render(request, 'product/partials/product-detail.html', context)
