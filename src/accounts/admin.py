from django.contrib import admin
from .models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'location', 'favorites_count', 'reviews_count', 'newsletter_subscription', 'created_at']
    list_filter = ['newsletter_subscription', 'email_notifications', 'created_at']
    search_fields = ['user__username', 'user__email', 'location', 'bio']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('User Information', {
            'fields': ('user', 'avatar', 'bio', 'location', 'website')
        }),
        ('Preferences', {
            'fields': ('newsletter_subscription', 'email_notifications')
        }),
        ('Favorites', {
            'fields': ('favorites',)
        }),
        ('Metadata', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

