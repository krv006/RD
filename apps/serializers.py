
from rest_framework import serializers
from .models import Category, Product, Contact_us, Partner, Redikt


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['name']


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()

    def get_category(self, obj):
        return obj.category.name if obj.category else None

    class Meta:
        model = Product
        fields = ['id', 'name', 'description_uz', 'description_ru', 'description_en', 'language', 'url', 'thumb', 'category', 'date']

class Contact_usSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact_us
        fields = ['id','address', 'email', 'phone_number' ]


class PartnerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Partner
        fields = ['id','image', 'url']


class RediktSerializer(serializers.ModelSerializer):

    class Meta:
        model = Redikt
        fields = ['id','name', 'description_place_uz', 'description_place_ru', 'description_place_en', 'image']

