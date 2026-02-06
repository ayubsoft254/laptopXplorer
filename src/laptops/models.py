from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify

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
