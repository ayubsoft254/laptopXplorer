from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Laptop(models.Model):
    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    specifications = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    review = models.TextField()    
    image = models.ImageField(upload_to='laptop_images/', blank=True, null=True)

    def __str__(self):
        return self.name

class Rating(models.Model):
    laptop = models.ForeignKey(Laptop, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()  # Ratings from 1 to 5, for example
    comment = models.TextField(blank=True, null=True)  # Optional comments

    class Meta:
        unique_together = ('laptop', 'user')

    def __str__(self):
        return self.name