from django.shortcuts import render, get_object_or_404
from shop.models import Category, Product
from cart.forms import CartAddProductForm
from django.core.paginator import Paginator
from urllib.parse import urlencode


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
    paginator = Paginator(products, 5)
    current_page = int(request.GET.get('page', 1))
    next_page_url, previous_page_url = None, None
    current_products = paginator.get_page(current_page)
    if current_products.has_next():
        next_page = urlencode({'page': current_products.next_page_number()})
        next_page_url = f'?{next_page}'
    if current_products.has_previous():
        previous_page = urlencode({'page': current_products.previous_page_number()})
        previous_page_url = f'?{previous_page}'

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        current_products = current_products.filter(category=category)

    context = {
        'category': category,
        'categories': categories,
        'products': current_products,
        'current_page': current_page,
        'prev_page_url': previous_page_url,
        'next_page_url': next_page_url,
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
