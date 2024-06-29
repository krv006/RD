from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

#! Bunga word ni qoshish ichiga 


class Product(models.Model):
    LANGUAGE_CHOICES = [
        ('uz', 'Uzbek'),
        ('ru', 'Russian'),
        ('en', 'English'),
    ]

    name = models.CharField(max_length=250)
    description_uz = CKEditor5Field()
    description_ru = CKEditor5Field()
    description_en = CKEditor5Field()
    language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES, default='uz')
    url = models.URLField()
    thumb = models.ImageField(upload_to='thumbs/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField(auto_now_add=True)
    doi = models.CharField(max_length=200,blank=True,null=True)
    best = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Contact_us(models.Model):
    address = models.CharField(max_length=1000)
    email = models.CharField(max_length=1000)
    phone_number = models.CharField(max_length=1000)

    def __str__(self):
        return self.address


class Partner(models.Model):
    image = models.ImageField(upload_to='thumbs/partners')
    url   = models.URLField()

    def __str__(self):
        return self.url

#! Bunga word ni qoshish ichiga 

class Redikt(models.Model):
    name= models.CharField(max_length=255)
    description_place_uz = CKEditor5Field()
    description_place_ru = CKEditor5Field()
    description_place_en = CKEditor5Field()
    image = models.ImageField(upload_to='editors')

    def __str__(self):
        return self.name
    