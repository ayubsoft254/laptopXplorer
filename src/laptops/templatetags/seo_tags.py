import json
from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag
def schema_org_json(data):
    """
    Convert Python dict to JSON-LD script tag for Schema.org structured data
    Usage: {% schema_org_json laptop.get_schema_org_data %}
    """
    # Remove None values
    cleaned_data = {k: v for k, v in data.items() if v is not None}
    json_str = json.dumps(cleaned_data, indent=2)
    return mark_safe(f'<script type="application/ld+json">\n{json_str}\n</script>')


@register.simple_tag
def og_meta_tag(property_name, content):
    """
    Generate Open Graph meta tag
    Usage: {% og_meta_tag "og:title" laptop.name %}
    """
    if not content:
        return ""
    return mark_safe(f'<meta property="{property_name}" content="{content}">')


@register.simple_tag
def twitter_meta_tag(name, content):
    """
    Generate Twitter Card meta tag
    Usage: {% twitter_meta_tag "twitter:title" laptop.name %}
    """
    if not content:
        return ""
    return mark_safe(f'<meta name="{name}" content="{content}">')


@register.simple_tag(takes_context=True)
def canonical_url(context):
    """
    Generate canonical URL tag
    Usage: {% canonical_url %}
    """
    request = context['request']
    full_url = request.build_absolute_uri(request.path)
    return mark_safe(f'<link rel="canonical" href="{full_url}">')


@register.simple_tag
def meta_description(content):
    """
    Generate meta description tag
    Usage: {% meta_description laptop.get_meta_description %}
    """
    if not content:
        return ""
    # Truncate to 160 characters for SEO best practices
    content = content[:160] if len(content) > 160 else content
    return mark_safe(f'<meta name="description" content="{content}">')


@register.simple_tag
def meta_keywords(keywords):
    """
    Generate meta keywords tag
    Usage: {% meta_keywords "laptop, gaming, review, specs" %}
    """
    if not keywords:
        return ""
    return mark_safe(f'<meta name="keywords" content="{keywords}">')


@register.filter
def to_keywords(laptop):
    """
    Generate comma-separated keywords from laptop object
    Usage: {{ laptop|to_keywords }}
    """
    keywords = [
        laptop.brand.name,
        laptop.name,
        laptop.category.name if laptop.category else "",
        laptop.processor.name if laptop.processor else "",
        f"{laptop.ram_size}GB RAM",
        laptop.storage_type,
        laptop.operating_system,
        "laptop review",
        "laptop specs",
        "buy laptop"
    ]
    return ", ".join([k for k in keywords if k])
