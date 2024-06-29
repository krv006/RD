from django.shortcuts import render
from django.shortcuts import render
from rest_framework.response import Response 
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Category, Contact_us, Partner, Product, Redikt
from .serializers import CategorySerializer, Contact_usSerializer, PartnerSerializer, ProductSerializer, RediktSerializer


class CategoryListAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



class Contact_usListAPIView(ListCreateAPIView):
    queryset = Contact_us.objects.all()
    serializer_class = Contact_usSerializer

class Contact_usRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Contact_us.objects.all()
    serializer_class = Contact_usSerializer



class PartnerListAPIView(ListCreateAPIView):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer

class PartnerRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer


class ProductListAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class RediktListAPIView(ListCreateAPIView):
    queryset = Redikt.objects.all()
    serializer_class = RediktSerializer

class RediktRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Redikt.objects.all()
    serializer_class = RediktSerializer
