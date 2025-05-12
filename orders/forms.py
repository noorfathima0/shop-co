from django import forms
from .models import ShippingInfo

class ShippingForm(forms.ModelForm):
    class Meta:
        model = ShippingInfo
        fields = ['full_name', 'address', 'city', 'postal_code', 'country']
