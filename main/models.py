from django.db import models
from datetime import  datetime

CATEGORY_CHOICES = (
    ('LR', 'Rayonnages lourds'),
    ('MI', 'Rayonnages mi-lourd'),
    ('LG', 'Rayonnages léger'),
    ('PR', 'Protection'),
    ('AC', 'Accessoires'),
)


# Create your models here.
class Product (models.Model):
    name = models.CharField(max_length= 50)
    slug = models.SlugField()
    description = models.TextField()
    image = models.ImageField(upload_to= 'products/images')
    category = models.CharField(choices= CATEGORY_CHOICES, max_length= 2)
    active = models.BooleanField(default=True)

    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Reference(models.Model):
    name = models.CharField(max_length=60)
    image = models.ImageField(upload_to= 'references/images')

    def __str__(self):
        return self.name
        