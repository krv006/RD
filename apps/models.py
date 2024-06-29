from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    LANGUAGE_CHOICES = [
        ('uz', 'Uzbek'),
        ('ru', 'Russian'),
        ('en', 'English'),
    ]

    name = models.CharField(max_length=250)
    description_uz = models.TextField()
    description_ru = models.TextField()
    description_en = models.TextField()
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


class Redikt(models.Model):
    name= models.CharField(max_length=255)
    description_place_uz = models.TextField()
    description_place_ru = models.TextField()
    description_place_en = models.TextField()
    image = models.ImageField(upload_to='editors')

    def __str__(self):
        return self.name