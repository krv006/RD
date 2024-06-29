from django.urls import path

from .views import CategoryListAPIView, CategoryRetrieveUpdateDestroyAPIView, Contact_usListAPIView, Contact_usRetrieveUpdateDestroyAPIView
from .views import  PartnerListAPIView, PartnerRetrieveUpdateDestroyAPIView, ProductListAPIView, ProductRetrieveUpdateDestroyAPIView, RediktRetrieveUpdateDestroyAPIView, RediktListAPIView 

urlpatterns = [
    path('category/', CategoryListAPIView.as_view(), name='category-list-create'),
    path('category/<int:pk>/', CategoryRetrieveUpdateDestroyAPIView.as_view(), name='category-retrieve-update-destroy'),

    path('contact/', Contact_usListAPIView.as_view(), name='contact-list-create'),
    path('contact/<int:pk>/', Contact_usRetrieveUpdateDestroyAPIView.as_view(), name='contact-retrieve-update-destroy'),

    path('partner/', PartnerListAPIView.as_view(), name='partner-list-create'),
    path('partner/<int:pk>/', PartnerRetrieveUpdateDestroyAPIView.as_view(), name='partner-retrieve-update-destroy'),

    path('product/', ProductListAPIView.as_view(), name='product-list-create'),
    path('product/<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view(), name='product-retrieve-update-destroy'),

    path('redikt/', RediktListAPIView.as_view(), name='redikt-list-create'),
    path('redikt/<int:pk>/', RediktRetrieveUpdateDestroyAPIView.as_view(), name='redikt-retrieve-update-destroy'),

]