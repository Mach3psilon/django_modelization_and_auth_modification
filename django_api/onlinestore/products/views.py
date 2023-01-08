from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.

from .models import Product, Manufacturer


class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'
