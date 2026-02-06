from django.db import models
from django.utils import timezone
from laptops.models import Laptop


class PriceHistory(models.Model):
    """Track price changes over time"""
    RETAILERS = [
        ('amazon', 'Amazon'),
        ('bestbuy', 'Best Buy'),
        ('newegg', 'Newegg'),
        ('walmart', 'Walmart'),
        ('direct', 'Direct from Manufacturer'),
        ('other', 'Other'),
    ]
    
    laptop = models.ForeignKey(Laptop, on_delete=models.CASCADE, related_name='price_history')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    retailer = models.CharField(max_length=20, choices=RETAILERS, default='direct')
    retailer_url = models.URLField(blank=True, help_text="Affiliate link")
    in_stock = models.BooleanField(default=True)
    recorded_at = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ['-recorded_at']
        verbose_name_plural = 'Price Histories'
        indexes = [
            models.Index(fields=['laptop', '-recorded_at']),
        ]
    
    def __str__(self):
        return f"{self.laptop.name} - ${self.price} ({self.recorded_at.date()})"
    
    @property
    def price_change_from_previous(self):
        """Calculate price change from previous record"""
        previous = PriceHistory.objects.filter(
            laptop=self.laptop,
            retailer=self.retailer,
            recorded_at__lt=self.recorded_at
        ).first()
        
        if previous:
            return float(self.price - previous.price)
        return 0
    
    @property
    def price_change_percentage(self):
        """Calculate percentage change from previous record"""
        previous = PriceHistory.objects.filter(
            laptop=self.laptop,
            retailer=self.retailer,
            recorded_at__lt=self.recorded_at
        ).first()
        
        if previous and previous.price > 0:
            return ((float(self.price) - float(previous.price)) / float(previous.price)) * 100
        return 0


class PriceAlert(models.Model):
    """User subscriptions for price drop alerts"""
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='price_alerts')
    laptop = models.ForeignKey(Laptop, on_delete=models.CASCADE, related_name='price_alerts')
    target_price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Alert when price drops below this")
    retailer = models.CharField(max_length=20, choices=PriceHistory.RETAILERS, blank=True, help_text="Specific retailer or any")
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_notified = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        ordering = ['-created_at']
        unique_together = ['user', 'laptop', 'retailer']
    
    def __str__(self):
        return f"{self.user.email} - {self.laptop.name} @ ${self.target_price}"
    
    def check_and_notify(self):
        """Check if current price meets target and notify user"""
        current_price = self.laptop.price
        
        if current_price <= self.target_price and self.active:
            # Send notification (implement email sending)
            from django.core.mail import send_mail
            send_mail(
                subject=f'Price Drop Alert: {self.laptop.name}',
                message=f'The price of {self.laptop.name} has dropped to ${current_price}! Your target was ${self.target_price}.',
                from_email='noreply@laptopxplorer.com',
                recipient_list=[self.user.email],
                fail_silently=True,
            )
            self.last_notified = timezone.now()
            self.save()
            return True
        return False
