from django import forms

from .models import Order,review,Help,Images

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            "ServiceType",
            "PreferredTime",
            "Description",
            "FromLocation"
        ]



class HelpForm(forms.ModelForm):
    class Meta:
        model = Help
        fields = [
            "Customer",
            "OrderWh",
            "I_type",
            "I_details"
        ]

class ImageForm(forms.Form):
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
