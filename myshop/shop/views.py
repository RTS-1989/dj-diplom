from django.shortcuts import render, get_object_or_404
from shop.models import Category, Product
from cart.forms import CartAddProductForm


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    template = 'shop/index.html'

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    context = {
        'category': category,
        'categories': categories,
        'products': products
    }

    return render(request, template, context)


def smartphones_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    template = 'shop/smartphones.html'

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    context = {
        'category': category,
        'categories': categories,
        'products': products
    }

    return render(request, template, context)


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id,
                                slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    template = 'shop/phone.html'
    context = {'product': product,
               'cart_product_form': cart_product_form}
    return render(request, template, context)
