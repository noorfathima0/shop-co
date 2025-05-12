from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from cart.models import CartItem
from .models import Order, OrderItem, ShippingInfo
from .forms import ShippingForm

@login_required
def checkout_view(request):
    cart_items = CartItem.objects.filter(session_key=request.session.session_key)
    if not cart_items:
        return redirect('cart:view_cart')

    if request.method == 'POST':
        form = ShippingForm(request.POST)
        if form.is_valid():
            order = Order.objects.create(
                user=request.user,
                is_paid=False  # simulate Cash on Delivery
            )
            for item in cart_items:
                OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    quantity=item.quantity
                )
            ShippingInfo.objects.create(order=order, **form.cleaned_data)
            cart_items.delete()
            return redirect('orders:order_success', order.id)
    else:
        form = ShippingForm()

    return render(request, 'orders/checkout.html', {'form': form, 'cart_items': cart_items})

@login_required
def order_success(request, order_id):
    return render(request, 'orders/order_success.html', {'order_id': order_id})

@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'orders/order_history.html', {'orders': orders})
