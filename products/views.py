from django.shortcuts import render
from rest_framework import viewsets
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer

# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class = ProductSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset=Category.objects.all()
    serializer_class = CategorySerializer

#class ProductList(generics.ListCreateAPIView):
#    queryset = Product.objects.all()
#    serializer_class = ProductSerializer

#class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
#    query = Product.objects.all()
#    serializer_class = ProductSerializer