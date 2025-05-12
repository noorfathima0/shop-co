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
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({'status': 'added'})
    return redirect('wishlist:wishlist_view')

@login_required
def remove_from_wishlist(request, product_id):
    WishlistItem.objects.filter(user=request.user, product_id=product_id).delete()
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({'status': 'removed'})
    return redirect('wishlist:wishlist_view')

from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

@csrf_exempt
@require_POST
@login_required
def toggle_wishlist(request):
    data = json.loads(request.body)
    product_id = data.get('product_id')
    product = get_object_or_404(Product, id=product_id)

    wishlist_item, created = WishlistItem.objects.get_or_create(user=request.user, product=product)

    if not created:
        wishlist_item.delete()
        return JsonResponse({'status': 'removed'})
    else:
        return JsonResponse({'status': 'added'})
