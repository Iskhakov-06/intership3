from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django_filters.views import FilterView

from .filters import ProductFilter
from .models import Product


class ProductListView(FilterView):
    model = Product
    template_name = 'book_shelf/product_list.html'
    context_object_name = 'products'
    filterset_class = ProductFilter


class ProductDetailView(DetailView):
    model = Product
    template_name = 'book_shelf/product_detail.html'
    context_object_name = 'product'


class ProductCreateView(CreateView):
    model = Product
    fields = ['name', 'price', 'manufacturer', 'warehouse', 'image']
    template_name = 'book_shelf/product_form.html'
    success_url = reverse_lazy('product_list')


class ProductUpdateView(UpdateView):
    model = Product
    fields = ['name', 'price', 'manufacturer', 'warehouse', 'image']
    template_name = 'book_shelf/product_form.html'
    success_url = reverse_lazy('product_list')


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'book_shelf/product_confirm_delete.html'
    success_url = reverse_lazy('product_list')
