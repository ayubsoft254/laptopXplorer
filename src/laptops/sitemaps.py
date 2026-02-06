from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Laptop, Brand, Category, Article


class LaptopSitemap(Sitemap):
    """Sitemap for laptop detail pages"""
    changefreq = "weekly"
    priority = 0.9
    
    def items(self):
        return Laptop.objects.filter(in_stock=True).order_by('-created_at')
    
    def lastmod(self, obj):
        return obj.updated_at
    
    def location(self, obj):
        return reverse('laptops:laptop_detail', args=[obj.slug])


class BrandSitemap(Sitemap):
    """Sitemap for brand pages"""
    changefreq = "monthly"
    priority = 0.7
    
    def items(self):
        return Brand.objects.all()
    
    def location(self, obj):
        return reverse('laptops:laptops_by_brand', args=[obj.slug])


class CategorySitemap(Sitemap):
    """Sitemap for category pages"""
    changefreq = "weekly"
    priority = 0.8
    
    def items(self):
        return Category.objects.all()
    
    def location(self, obj):
        # If you have a category filter URL, use it here
        # For now, return laptop list with category filter
        return f"{reverse('laptops:laptop_list')}?category={obj.id}"


class ArticleSitemap(Sitemap):
    """Sitemap for article/review pages"""
    changefreq = "monthly"
    priority = 0.6
    
    def items(self):
        return Article.objects.filter(published=True).order_by('-created_at')
    
    def lastmod(self, obj):
        return obj.updated_at
    
    def location(self, obj):
        return reverse('laptops:article_detail', args=[obj.slug])


class StaticViewSitemap(Sitemap):
    """Sitemap for static pages"""
    priority = 0.5
    changefreq = 'monthly'
    
    def items(self):
        return ['laptops:home', 'laptops:laptop_list', 'laptops:about', 'laptops:contact']
    
    def location(self, item):
        return reverse(item)
