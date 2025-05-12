# wishlist/templatetags/wishlist_tags.py
from django import template
from wishlist.models import WishlistItem

register = template.Library()

@register.filter(name='in_wishlist')
def in_wishlist(product, user):
    if not user.is_authenticated:
        return False
    return WishlistItem.objects.filter(user=user, product=product).exists()
