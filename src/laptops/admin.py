from django.contrib import admin
from .models import Brand, Category, Processor, Laptop


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name', 'website', 'created_at']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'icon']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']


@admin.register(Processor)
class ProcessorAdmin(admin.ModelAdmin):
    list_display = ['name', 'brand', 'cores', 'threads', 'base_clock']
    list_filter = ['brand']
    search_fields = ['name', 'generation']
    list_per_page = 50


@admin.register(Laptop)
class LaptopAdmin(admin.ModelAdmin):
    list_display = ['name', 'brand', 'category', 'processor', 'ram_size', 'storage_size', 'price', 'in_stock', 'created_at']
    list_filter = ['brand', 'category', 'in_stock', 'operating_system', 'graphics_type', 'ram_type']
    search_fields = ['name', 'model_number', 'description']
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ['created_at', 'updated_at', 'views']
    list_editable = ['in_stock']
    list_per_page = 25
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'slug', 'brand', 'category', 'model_number', 'description', 'image')
        }),
        ('Processor', {
            'fields': ('processor',)
        }),
        ('Memory & Storage', {
            'fields': ('ram_size', 'ram_type', 'ram_upgradeable', 'max_ram', 
                      'storage_size', 'storage_type', 'additional_storage')
        }),
        ('Display', {
            'fields': ('display_size', 'display_resolution', 'refresh_rate', 
                      'panel_type', 'touchscreen')
        }),
        ('Graphics', {
            'fields': ('graphics_type', 'graphics_model', 'graphics_memory')
        }),
        ('Battery & Physical', {
            'fields': ('battery_capacity', 'battery_life', 'weight', 
                      'dimensions', 'color')
        }),
        ('Connectivity', {
            'fields': ('wifi', 'bluetooth', 'ports', 'webcam')
        }),
        ('System & Pricing', {
            'fields': ('operating_system', 'price', 'currency', 'in_stock', 'release_date')
        }),
        ('Additional', {
            'fields': ('features', 'additional_images', 'views', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('brand', 'category', 'processor')
