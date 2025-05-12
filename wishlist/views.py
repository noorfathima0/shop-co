from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from product.models import Product
from .models import WishlistItem

@login_required
def wishlist_view(request):
    items = WishlistItem.objects.filter(user=request.user)
    return render(request, 'wishlist/wishlist.html', {'wishlist_items': items})

@login_required
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    WishlistItem.objects.get_or_create(user=request.user, product=product)
    return redirect('wishlist:wishlist_view')

@login_required
def remove_from_wishlist(request, product_id):
    WishlistItem.objects.filter(user=request.user, product__id=product_id).delete()
    return redirect('wishlist:wishlist_view')
