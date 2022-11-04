from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect

from catalog.forms import CommentForm
from catalog.models import Product


def paginator(request, products_list):
    paginator = Paginator(products_list, settings.SLICE)
    page_number = request.GET.get('page', 1)
    products = paginator.get_page(page_number)
    return products

def index(request):
    template = 'catalog/index.html'
    products_list = Product.objects.order_by('price')
    products = paginator(request, products_list)
    context = {
        'products': products,
    }
    return render(request, template, context)


def sort(request):
    template = 'catalog/index.html'
    products_list = Product.objects.order_by('-price')
    products = paginator(request, products_list)
    context = {
        'products': products,
    }
    return render(request, template, context)


def product_detail(request, product_id):
    template = 'catalog/product_detail.html'
    product = get_object_or_404(Product, pk=product_id)
    comments = product.comments.all()

    context = {
        'product': product,
        'form': CommentForm(),
        'comments': comments,
    }
    return render(request, template, context)


@login_required
def add_comment(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.author = request.user
        comment.product = product
        comment.save()
    return redirect('catalog:product_detail', product_id=product_id)
