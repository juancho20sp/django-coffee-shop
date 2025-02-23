from django import forms
from .models import Product


class ProductForm(forms.Form):
    name = forms.CharField(max_length=200, label="Product Name")
    description = forms.CharField(max_length=300, label="Product Description")
    price = forms.DecimalField(max_digits=5, decimal_places=2, label="Product Price")
    available = forms.BooleanField(
        initial=True, label="Product Availability", required=False
    )
    photo = forms.ImageField(label="Product Photo", required=False)

    def save(self):
        Product.objects.create(
            name=self.cleaned_data["name"],
            description=self.cleaned_data["description"],
            price=self.cleaned_data["price"],
            available=self.cleaned_data["available"],
            photo=self.cleaned_data["photo"],
        )
