from django.contrib import admin
from .models import Brand, Category, Processor, Laptop, Review, Article, PriceHistory, PriceAlert, LaptopImage


class LaptopImageInline(admin.TabularInline):
    model = LaptopImage
    extra = 3
    fields = ['image', 'caption', 'is_primary', 'order']
    readonly_fields = []


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
    inlines = [LaptopImageInline]  # Add image gallery inline
    
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


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'laptop', 'rating', 'verified', 'created_at', 'helpful_count']
    list_filter = ['rating', 'verified', 'created_at']
    search_fields = ['user_name', 'title', 'comment', 'laptop__name']
    readonly_fields = ['created_at', 'helpful_count']
    list_editable = ['verified']
    list_per_page = 50
    
    fieldsets = (
        ('Review Information', {
            'fields': ('laptop', 'user_name', 'email', 'rating', 'verified')
        }),
        ('Content', {
            'fields': ('title', 'comment', 'pros', 'cons')
        }),
        ('Meta', {
            'fields': ('helpful_count', 'created_at'),
            'classes': ('collapse',)
        }),
    )
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('laptop', 'laptop__brand')


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'laptop', 'author_name', 'published', 'featured', 'read_time', 'views', 'created_at']
    list_filter = ['published', 'featured', 'created_at']
    search_fields = ['title', 'author_name', 'content', 'laptop__name']
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ['created_at', 'updated_at', 'views', 'likes']
    list_editable = ['published', 'featured']
    list_per_page = 25
    

@admin.register(PriceHistory)
class PriceHistoryAdmin(admin.ModelAdmin):
    list_display = ['laptop', 'price', 'retailer', 'in_stock', 'recorded_at']
    list_filter = ['retailer', 'in_stock', 'recorded_at']
    search_fields = ['laptop__name', 'laptop__brand__name']
    readonly_fields = ['recorded_at']
    date_hierarchy = 'recorded_at'
    list_per_page = 50
    
    fieldsets = (
        ('Laptop Information', {
            'fields': ('laptop',)
        }),
        ('Price Details', {
            'fields': ('price', 'retailer', 'retailer_url', 'in_stock')
        }),
        ('Timestamp', {
            'fields': ('recorded_at',)
        }),
    )


@admin.register(PriceAlert)
class PriceAlertAdmin(admin.ModelAdmin):
    list_display = ['user', 'laptop', 'target_price', 'retailer', 'active', 'created_at', 'last_notified']
    list_filter = ['active', 'retailer', 'created_at']
    search_fields = ['user__email', 'laptop__name']
    readonly_fields = ['created_at', 'last_notified']
    list_editable = ['active']
    list_per_page = 50
    
    fieldsets = (
        ('Alert Information', {
            'fields': ('user', 'laptop', 'target_price', 'retailer')
        }),
        ('Status', {
            'fields': ('active',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'last_notified'),
            'classes': ('collapse',)
        }),
    )


@admin.register(LaptopImage)
class LaptopImageAdmin(admin.ModelAdmin):
    list_display = ['laptop', 'caption', 'is_primary', 'order', 'uploaded_at']
    list_filter = ['is_primary', 'uploaded_at']
    search_fields = ['laptop__name', 'caption']
    list_editable = ['is_primary', 'order']
    readonly_fields = ['uploaded_at']
    list_per_page = 50
    
    fieldsets = (
        ('Article Information', {
            'fields': ('title', 'slug', 'laptop', 'author_name', 'author_bio')
        }),
        ('Content', {
            'fields': ('featured_image', 'excerpt', 'content')
        }),
        ('Metadata', {
            'fields': ('read_time', 'published', 'featured')
        }),
        ('Stats', {
            'fields': ('views', 'likes', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('laptop', 'laptop__brand')

