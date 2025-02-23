from django.urls import reverse_lazy
from django.views import generic
from .forms import ProductForm
from .models import Product


# Create your views here.
class ProductFormView(generic.FormView):
    template_name = "products/add_product.html"
    form_class = ProductForm
    # Después de crear el producto, redirigir a la misma página
    success_url = reverse_lazy("add_product")

    # Esto se ejecuta después de que el formulario se envía correctamente
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ProductListView(generic.ListView):
    model = Product
    template_name = "products/product_list.html"
    context_object_name = "products"
