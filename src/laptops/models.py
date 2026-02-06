from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify
from django.urls import reverse

class Brand(models.Model):
    """Laptop brand/manufacturer"""
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    logo = models.ImageField(upload_to='brands/', blank=True, null=True)
    description = models.TextField(blank=True)
    website = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['name']
        
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name


class Category(models.Model):
    """Laptop categories (Gaming, Business, Ultrabook, etc.)"""
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    description = models.TextField(blank=True)
    icon = models.CharField(max_length=50, blank=True, help_text="CSS icon class")
    
    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Categories'
        
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name


class Processor(models.Model):
    """CPU/Processor information"""
    PROCESSOR_BRANDS = [
        ('Intel', 'Intel'),
        ('AMD', 'AMD'),
        ('Apple', 'Apple Silicon'),
        ('Other', 'Other'),
    ]
    
    name = models.CharField(max_length=200, unique=True)
    brand = models.CharField(max_length=20, choices=PROCESSOR_BRANDS)
    generation = models.CharField(max_length=50, blank=True)
    cores = models.PositiveIntegerField(blank=True, null=True)
    threads = models.PositiveIntegerField(blank=True, null=True)
    base_clock = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True, help_text="GHz")
    boost_clock = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True, help_text="GHz")
    
    class Meta:
        ordering = ['brand', 'name']
        
    def __str__(self):
        return self.name


class Laptop(models.Model):
    """Main laptop model with comprehensive specifications"""
    
    # Display panel types
    PANEL_TYPES = [
        ('IPS', 'IPS'),
        ('OLED', 'OLED'),
        ('TN', 'TN'),
        ('VA', 'VA'),
        ('Mini-LED', 'Mini-LED'),
    ]
    
    # Storage types
    STORAGE_TYPES = [
        ('SSD', 'SSD (NVMe/SATA)'),
        ('HDD', 'HDD'),
        ('eMMC', 'eMMC'),
        ('Hybrid', 'Hybrid (SSD + HDD)'),
    ]
    
    # RAM types
    RAM_TYPES = [
        ('DDR4', 'DDR4'),
        ('DDR5', 'DDR5'),
        ('LPDDR4', 'LPDDR4'),
        ('LPDDR5', 'LPDDR5'),
    ]
    
    # Graphics types
    GRAPHICS_TYPES = [
        ('Integrated', 'Integrated'),
        ('Dedicated', 'Dedicated'),
        ('Hybrid', 'Hybrid'),
    ]
    
    # Operating Systems
    OS_CHOICES = [
        ('Windows 11', 'Windows 11'),
        ('Windows 10', 'Windows 10'),
        ('macOS', 'macOS'),
        ('Linux', 'Linux'),
        ('Chrome OS', 'Chrome OS'),
        ('DOS', 'DOS/No OS'),
    ]
    
    # Basic Information
    name = models.CharField(max_length=300)
    slug = models.SlugField(max_length=300, unique=True, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='laptops')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='laptops')
    model_number = models.CharField(max_length=100, blank=True)
    
    # Processor
    processor = models.ForeignKey(Processor, on_delete=models.SET_NULL, null=True, blank=True)
    
    # Memory (RAM)
    ram_size = models.PositiveIntegerField(help_text="GB")
    ram_type = models.CharField(max_length=20, choices=RAM_TYPES, default='DDR4')
    ram_upgradeable = models.BooleanField(default=False)
    max_ram = models.PositiveIntegerField(blank=True, null=True, help_text="Maximum RAM in GB")
    
    # Storage
    storage_size = models.PositiveIntegerField(help_text="GB")
    storage_type = models.CharField(max_length=20, choices=STORAGE_TYPES, default='SSD')
    additional_storage = models.BooleanField(default=False, help_text="Has additional storage slot")
    
    # Display
    display_size = models.DecimalField(max_digits=4, decimal_places=2, help_text="Inches")
    display_resolution = models.CharField(max_length=50, help_text="e.g., 1920x1080")
    refresh_rate = models.PositiveIntegerField(default=60, help_text="Hz")
    panel_type = models.CharField(max_length=20, choices=PANEL_TYPES, default='IPS')
    touchscreen = models.BooleanField(default=False)
    
    # Graphics
    graphics_type = models.CharField(max_length=20, choices=GRAPHICS_TYPES, default='Integrated')
    graphics_model = models.CharField(max_length=200, blank=True)
    graphics_memory = models.PositiveIntegerField(blank=True, null=True, help_text="GB (for dedicated)")
    
    # Battery
    battery_capacity = models.PositiveIntegerField(blank=True, null=True, help_text="Wh")
    battery_life = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True, help_text="Hours")
    
    # Physical
    weight = models.DecimalField(max_digits=4, decimal_places=2, help_text="kg")
    dimensions = models.CharField(max_length=100, blank=True, help_text="L x W x H (mm)")
    color = models.CharField(max_length=50, blank=True)
    
    # Connectivity
    wifi = models.CharField(max_length=50, default="Wi-Fi 6")
    bluetooth = models.CharField(max_length=20, default="5.0")
    ports = models.TextField(blank=True, help_text="USB, HDMI, etc.")
    webcam = models.CharField(max_length=100, blank=True)
    
    # Operating System
    operating_system = models.CharField(max_length=50, choices=OS_CHOICES, default='Windows 11')
    
    # Pricing & Availability
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, default='USD')
    in_stock = models.BooleanField(default=True)
    
    # Media
    image = models.ImageField(upload_to='laptops/', blank=True, null=True)
    additional_images = models.TextField(blank=True, help_text="Comma-separated image URLs")
    
    # Additional Info
    release_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True)
    features = models.TextField(blank=True, help_text="Key features, one per line")
    
    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    views = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['-created_at']
        
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(f"{self.brand.name} {self.name}")
            self.slug = base_slug
            counter = 1
            while Laptop.objects.filter(slug=self.slug).exists():
                self.slug = f"{base_slug}-{counter}"
                counter += 1
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.brand.name} {self.name}"
    
    @property
    def full_name(self):
        return f"{self.brand.name} {self.name} ({self.processor.name if self.processor else 'N/A'})"
    
    @property
    def display_info(self):
        return f"{self.display_size}\" {self.display_resolution} {self.refresh_rate}Hz {self.panel_type}"
    
    @property
    def ram_info(self):
        return f"{self.ram_size}GB {self.ram_type}"
    
    @property
    def storage_info(self):
        return f"{self.storage_size}GB {self.storage_type}"
    
    @property
    def average_rating(self):
        """Calculate average rating from reviews"""
        reviews = self.reviews.all()
        if reviews.exists():
            return round(sum(r.rating for r in reviews) / reviews.count(), 1)
        return 0
    
    @property
    def review_count(self):
        """Get total number of reviews"""
        return self.reviews.count()
    
    @property
    def lowest_price_ever(self):
        """Get the lowest price from price history"""
        history = self.price_history.all()
        if history.exists():
            return min(h.price for h in history)
        return self.price
    
    @property
    def price_trend(self):
        """Get price trend: 'up', 'down', or 'stable'"""
        recent = self.price_history.all()[:2]
        if len(recent) >= 2:
            if recent[0].price < recent[1].price:
                return 'down'
            elif recent[0].price > recent[1].price:
                return 'up'
        return 'stable'
    
    @property
    def price_change_percentage(self):
        """Get price change percentage from previous record"""
        recent = self.price_history.all()[:2]
        if len(recent) >= 2:
            old_price = float(recent[1].price)
            new_price = float(recent[0].price)
            if old_price > 0:
                return ((new_price - old_price) / old_price) * 100
        return 0
    
    @property
    def primary_image(self):
        """Get the primary display image"""
        primary = self.images.filter(is_primary=True).first()
        if primary:
            return primary.image
        # Fallback to first image if no primary set
        first_image = self.images.first()
        if first_image:
            return first_image.image
        # Finally fallback to the old single image field
        return self.image
    
    @property
    def gallery_images(self):
        """Get all gallery images excluding primary"""
        return self.images.filter(is_primary=False)
    
    def get_absolute_url(self):
        """Return canonical URL for this laptop"""
        return reverse('laptops:laptop_detail', args=[self.slug])
    
    def get_meta_description(self):
        """Generate SEO-friendly meta description"""
        return (
            f"{self.brand.name} {self.name} with {self.processor.name if self.processor else 'powerful processor'}, "
            f"{self.ram_size}GB RAM, {self.storage_size}GB {self.storage_type}, "
            f"{self.display_size}\" {self.display_resolution} display. "
            f"Price: ${self.price}. {self.review_count} reviews. "
            f"{'In stock' if self.in_stock else 'Out of stock'}."
        )
    
    def get_schema_org_data(self):
        """Generate Schema.org Product structured data (JSON-LD)"""
        return {
            "@context": "https://schema.org/",
            "@type": "Product",
            "name": f"{self.brand.name} {self.name}",
            "image": self.primary_image.url if self.primary_image else "",
            "description": self.description or self.get_meta_description(),
            "brand": {
                "@type": "Brand",
                "name": self.brand.name
            },
            "offers": {
                "@type": "Offer",
                "url": self.get_absolute_url(),
                "priceCurrency": self.currency,
                "price": str(self.price),
                "availability": "https://schema.org/InStock" if self.in_stock else "https://schema.org/OutOfStock",
                "itemCondition": "https://schema.org/NewCondition"
            },
            "aggregateRating": {
                "@type": "AggregateRating",
                "ratingValue": str(self.average_rating),
                "reviewCount": str(self.review_count),
                "bestRating": "5",
                "worstRating": "1"
            } if self.review_count > 0 else None,
            "review": [
                {
                    "@type": "Review",
                    "reviewRating": {
                        "@type": "Rating",
                        "ratingValue": str(review.rating),
                        "bestRating": "5",
                        "worstRating": "1"
                    },
                    "author": {
                        "@type": "Person",
                        "name": review.user_name
                    },
                    "reviewBody": review.comment,
                    "datePublished": review.created_at.isoformat()
                }
                for review in self.reviews.all()[:5]  # Include top 5 reviews
            ] if self.review_count > 0 else []
        }


class Review(models.Model):
    """Laptop reviews and ratings"""
    laptop = models.ForeignKey(Laptop, on_delete=models.CASCADE, related_name='reviews')
    user_name = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        help_text="Rating from 1 to 5 stars"
    )
    title = models.CharField(max_length=200)
    comment = models.TextField()
    pros = models.TextField(blank=True, help_text="What you liked")
    cons = models.TextField(blank=True, help_text="What could be better")
    helpful_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    verified = models.BooleanField(default=False, help_text="Verified purchase")
    
    class Meta:
        ordering = ['-created_at']
        
    def __str__(self):
        return f"{self.user_name} - {self.laptop.name} ({self.rating}⭐)"
    
    @property
    def rating_stars(self):
        """Return rating as stars"""
        return '⭐' * self.rating


class Article(models.Model):
    """Editorial articles and in-depth reviews about laptops"""
    laptop = models.ForeignKey(Laptop, on_delete=models.CASCADE, related_name='articles')
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    author_name = models.CharField(max_length=100)
    author_bio = models.TextField(blank=True, help_text="Short bio about the author")
    featured_image = models.ImageField(upload_to='articles/', blank=True, null=True)
    excerpt = models.TextField(max_length=300, help_text="Short description for previews")
    content = models.TextField(help_text="Full article content (supports HTML)")
    
    # Article metadata
    read_time = models.IntegerField(default=5, help_text="Estimated reading time in minutes")
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    
    # Publishing
    published = models.BooleanField(default=True)
    featured = models.BooleanField(default=False, help_text="Show on homepage")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while Article.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title
    
    @property
    def formatted_read_time(self):
        """Return formatted read time"""
        return f"{self.read_time} min read"
    
    def get_absolute_url(self):
        """Return canonical URL for this article"""
        return reverse('laptops:article_detail', args=[self.slug])
    
    def get_meta_description(self):
        """Return SEO-friendly meta description"""
        return self.excerpt or self.content[:160]
    
    def get_schema_org_data(self):
        """Generate Schema.org Article structured data (JSON-LD)"""
        return {
            "@context": "https://schema.org",
            "@type": "Article",
            "headline": self.title,
            "image": self.featured_image.url if self.featured_image else "",
            "author": {
                "@type": "Person",
                "name": self.author_name,
                "description": self.author_bio
            },
            "publisher": {
                "@type": "Organization",
                "name": "LaptopXplorer",
                "logo": {
                    "@type": "ImageObject",
                    "url": "/static/logo.png"  # Update with actual logo URL
                }
            },
            "datePublished": self.created_at.isoformat(),
            "dateModified": self.updated_at.isoformat(),
            "description": self.excerpt,
            "articleBody": self.content,
            "mainEntityOfPage": {
                "@type": "WebPage",
                "@id": self.get_absolute_url()
            }
        }


# Price Tracking Models
from django.utils import timezone

from django.contrib.auth.models import User


class LaptopImage(models.Model):
    """Multiple images for a laptop (gallery)"""
    laptop = models.ForeignKey(Laptop, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='laptop_gallery/')
    caption = models.CharField(max_length=200, blank=True)
    is_primary = models.BooleanField(default=False, help_text="Main display image")
    order = models.PositiveIntegerField(default=0, help_text="Display order")
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-is_primary', 'order', '-uploaded_at']
        verbose_name = 'Laptop Image'
        verbose_name_plural = 'Laptop Images'
    
    def __str__(self):
        return f"{self.laptop.name} - Image {self.order}"
    
    def save(self, *args, **kwargs):
        # If this is marked as primary, unmark others for this laptop
        if self.is_primary:
            LaptopImage.objects.filter(laptop=self.laptop, is_primary=True).update(is_primary=False)
        super().save(*args, **kwargs)


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


class PriceAlert(models.Model):
    """User subscriptions for price drop alerts"""
    from django.contrib.auth.models import User
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='price_alerts')
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
