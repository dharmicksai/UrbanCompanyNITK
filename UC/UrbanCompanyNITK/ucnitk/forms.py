from django import forms

from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            "ServiceType",
            "PreferredTime",
            "Description",
            "FromLocation"
        ]
class reviewForm(forms.ModelForm):
    class Meta:
        model = review
        fields = [
            "ServiceType",
            "rating",
            "review"
        ]
