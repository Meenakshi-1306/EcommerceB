# store/views.py

from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer

class ProductListCreate(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
from django.views.generic import TemplateView

class FrontendAppView(TemplateView):
    template_name = 'index.html'
