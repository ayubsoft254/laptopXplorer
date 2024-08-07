from django.db import models

# Create your models here.
class Laptop(models.Model):
    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=100)
    specifications = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    review = models.TextField()
    rating = models.FloatField()
    image = models.ImageField(upload_to='static/', blank=True, null=True)

    def __str__(self):
        return self.name