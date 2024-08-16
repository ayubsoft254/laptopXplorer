from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg
from django.core.exceptions import ValidationError

# Create your models here.
class Brand(models.Model):  
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='staticfiles/img/brand_imgs', blank=True, null=True)    

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Laptop(models.Model):
    name = models.CharField(max_length=200)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='laptops')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    model = models.CharField(max_length=100)
    specifications = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)       
    image = models.ImageField(upload_to='staticfiles/img/laptop_imgs', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    average_rating = models.FloatField(default=0.0)  

    def __str__(self):
        return self.name

    @property
    def average_rating(self):
        ratings = self.rating_set.all()
        if ratings.exists():
            return ratings.aggregate(Avg('score'))['score__avg']
        return None 

    @property
    def comments(self):
        ratings = self.rating_set.all()
        comments = [rating.comment for rating in ratings if rating.comment]
        return " ".join(comments) if comments else "No reviews yet"    
    
    
class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    laptop = models.ForeignKey(Laptop, on_delete=models.CASCADE)
    score = models.PositiveIntegerField()
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'laptop')

    def __str__(self):
        return f'{self.user.username} rated {self.laptop.name} with {self.score}'

    def save(self, *args, **kwargs):
        if not (1 <= self.score <= 5):
            raise ValueError("Score must be between 1 and 5")
        super().save(*args, **kwargs)