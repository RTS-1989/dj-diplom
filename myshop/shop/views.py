from django.shortcuts import render, get_object_or_404
from shop.models import Subcategory, Product, Review
from cart.forms import CartAddProductForm
from .forms import UserReviewAddForm
from django.core.paginator import Paginator
from urllib.parse import urlencode
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import get_user_model


def index(request):

    products = Product.objects.filter(available=True)
    template = 'shop/index.html'

    context = {
        'products': products
    }

    return render(request, template, context)


def product_categories(request, category_slug=None):

    cart_product_form = CartAddProductForm()
    template = 'shop/categories.html'
    current_category = get_object_or_404(Subcategory, slug=category_slug)
    current_products = current_category.products.all()

    paginator = Paginator(current_products, 5)
    current_page = int(request.GET.get('page', 1))
    current_products = paginator.get_page(current_page)
    next_page_url, previous_page_url = None, None
    if current_products.has_next():
        next_page = urlencode({'page': current_products.next_page_number()})
        next_page_url = f'?{next_page}'
    if current_products.has_previous():
        previous_page = urlencode({'page': current_products.previous_page_number()})
        previous_page_url = f'?{previous_page}'

    context = {
        'current_category': current_category,
        'current_products': current_products,
        'cart_product_form': cart_product_form,
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


def review(request):
    if request.method == 'POST':
        id = request.POST.get('id', None)
        form = UserReviewAddForm()
        if id:
            try:
                review = Review.objects.get(pk=id)
            except ObjectDoesNotExist:
                return ()
            if form.is_valid():
                form = form.save(commit=False)
                form.user = get_user_model()
                form.review = review
                form.save()
                return ()
            return ()
        return()

    context = {'form': UserReviewAddForm(),
               'reviews': Review.objects.all()
               }

    return render(request, 'shop/index.html', context)


