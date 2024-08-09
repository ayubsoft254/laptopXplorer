from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Brand(models.Model):
    """
    Represents a laptop.

    Attributes:
        name (str): The name of the laptop.
        brand (Brand): The brand of the laptop.
        model (str): The model number of the laptop.
        specifications (str): The specifications of the laptop.
        price (Decimal): The price of the laptop.
        review (str): A review of the laptop.
        image (ImageField): An image of the laptop.
        created_at (DateTime): The date and time the laptop was added.

    Example:
        >>> brand = Brand.objects.get(name="Apple")
        >>> laptop = Laptop(name="MacBook Air", brand=brand, model="A1466", 
                            specifications="Intel Core i5, 8GB RAM, 256GB SSD", 
                            price=999.99, review="A great laptop for everyday use.")
        >>> laptop.save()
    """
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='staticfiles/img/brand_imgs', blank=True, null=True)    

    def __str__(self):
        return self.name

class Laptop(models.Model):
    name = models.CharField(max_length=200)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='laptops')
    model = models.CharField(max_length=100)
    specifications = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    review = models.TextField()    
    image = models.ImageField(upload_to='staticfiles/img/laptop_imgs', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.brand.name})"