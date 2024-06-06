from django.db import models

# Create your models here.
class Laptop(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    processor_family = models.CharField(max_length=100, blank=True, null=True)
    processor_details = models.CharField(max_length=255, blank=True, null=True)
    graphics = models.CharField(max_length=100, blank=True, null=True)
    ram = models.CharField(max_length=100)
    storage = models.CharField(max_length=100)
    internal_drive = models.CharField(max_length=100, blank=True, null=True)
    display_size = models.CharField(max_length=100)
    display_details = models.CharField(max_length=255, blank=True, null=True)  # e.g., resolution, touch, IPS, brightness, NTSC
    security_software_license = models.CharField(max_length=255, blank=True, null=True)
    ports = models.CharField(max_length=255, blank=True, null=True)
    expansion_slots = models.CharField(max_length=100, blank=True, null=True)
    audio_features = models.CharField(max_length=255, blank=True, null=True)
    webcam_details = models.CharField(max_length=255, blank=True, null=True)
    keyboard_features = models.CharField(max_length=255, blank=True, null=True)  # e.g., type, backlit, spill resistant
    pointing_device = models.CharField(max_length=255, blank=True, null=True)
    wifi = models.CharField(max_length=100, blank=True, null=True)
    bluetooth = models.CharField(max_length=100, blank=True, null=True)
    wwan = models.CharField(max_length=100, blank=True, null=True)
    power_supply = models.CharField(max_length=100, blank=True, null=True)
    battery = models.CharField(max_length=100, blank=True, null=True)
    color = models.CharField(max_length=100, blank=True, null=True)
    energy_efficiency = models.CharField(max_length=255, blank=True, null=True)
    dimensions = models.CharField(max_length=100, blank=True, null=True)
    weight = models.CharField(max_length=100, blank=True, null=True)
    warranty = models.CharField(max_length=255, blank=True, null=True)
    support_service = models.CharField(max_length=255, blank=True, null=True)
    software_included = models.CharField(max_length=255, blank=True, null=True)
    manageability_features = models.CharField(max_length=255, blank=True, null=True)
    security_management = models.CharField(max_length=255, blank=True, null=True)
    sustainable_impact = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField()
    image = models.ImageField(upload_to='laptops/', blank=True, null=True)
    release_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.brand} {self.model}"