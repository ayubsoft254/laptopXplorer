from django.db import models
from django.contrib.auth.models import User

# Ensure Laptop model is defined before Rating model
class Laptop(models.Model):
    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=100)
    specifications = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    review = models.TextField()
    image = models.ImageField(upload_to='laptops/', blank=True, null=True)

    def __str__(self):
        return self.name

    @property
    def average_rating(self):
        ratings = self.rating_set.all()
        if ratings:
            return sum(r.score for r in ratings) / len(ratings)
        return 0

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    laptop = models.ForeignKey(Laptop, on_delete=models.CASCADE)
    score = models.IntegerField(choices=[(i, i) for i in range(1, 6)])

    class Meta:
        unique_together = ('user', 'laptop')

    def __str__(self):
        return f"{self.user.username} rated {self.laptop.name}: {self.score}"
