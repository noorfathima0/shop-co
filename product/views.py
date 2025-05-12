from django.shortcuts import render, get_object_or_404
from .models import Product
from django.db.models import Q
from django.http import JsonResponse


def product_list(request):
    query = request.GET.get('q', '')
    if query:
        products = Product.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
    else:
        products = Product.objects.all()

    return render(request, 'product/product_list.html', {'products': products})


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product/product_detail.html', {'product': product})

def search_suggestions(request):
    query = request.GET.get('q', '')
    suggestions_list = []

    if query:
        suggestions = Product.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        ).values('name')[:5]  # Limit to the top 5 results
        
        suggestions_list = [product['name'] for product in suggestions]

    return JsonResponse(suggestions_list, safe=False)