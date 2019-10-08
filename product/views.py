from django.shortcuts import render, get_object_or_404

# Create your views here.
from product.models import Product, ProductImage


def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    productimage = ProductImage.objects.filter(product_id=product_id)
    context = {
               'productimage': productimage,
               'product': product,

               }

    return render(request, 'detail.html', context)