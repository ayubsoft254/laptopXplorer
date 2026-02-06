# 🎯 SEO Features - Quick Start

## Installation

Run the setup script:
```bash
deploy_seo.bat
```

This will:
1. Run migrations (if needed)
2. Collect static files
3. Test SEO endpoints
4. Display setup confirmation

## Testing

### Test SEO Components (Python)
```bash
cd C:\Users\henry\Desktop\laptopXplorer
python test_seo.py
```

### Test Live Endpoints
```bash
# Start server
cd src
python manage.py runserver

# Visit these URLs:
http://localhost:8000/sitemap.xml
http://localhost:8000/robots.txt
```

### Test in Browser
1. Go to any laptop detail page
2. Right-click → View Page Source
3. Search for:
   - `<meta name="description">`
   - `<meta property="og:`
   - `<script type="application/ld+json">`
   - `<link rel="canonical"`

## What's Included

### ✅ 1. Meta Tags (Every Page)
- Description, keywords, author
- Robots directive
- Viewport (mobile-friendly)

### ✅ 2. Open Graph (Social Media)
- Facebook link previews
- LinkedIn rich cards
- Custom images & descriptions

### ✅ 3. Twitter Cards
- Large image cards
- Title, description, image

### ✅ 4. Schema.org Structured Data
**Product Schema** (Laptops):
- Name, price, availability
- Brand information
- Aggregate ratings
- Individual reviews

**Article Schema** (Reviews):
- Headline, author, dates
- Publisher info
- Featured image

**Organization Schema** (Site-wide):
- Company name & logo
- Social media links

### ✅ 5. XML Sitemaps
5 separate sitemaps:
- Laptops (priority 0.9)
- Brands (priority 0.7)
- Articles (priority 0.6)
- Categories (priority 0.8)
- Static pages (priority 0.5)

### ✅ 6. robots.txt
- Allows search engine crawling
- Blocks admin/account pages
- Points to sitemap

### ✅ 7. Canonical URLs
- Prevents duplicate content
- On every page

### ✅ 8. Custom Template Tags
```django
{% load seo_tags %}

{# Add Schema.org JSON-LD #}
{% schema_org_json laptop.get_schema_org_data %}

{# Generate keywords #}
{{ laptop|to_keywords }}

{# Add meta description #}
{% meta_description "Your description" %}
```

## Files Created

```
laptopXplorer/
├── src/
│   ├── laptops/
│   │   ├── sitemaps.py         # Sitemap configuration
│   │   ├── templatetags/
│   │   │   ├── __init__.py
│   │   │   └── seo_tags.py     # Custom SEO tags
│   │   ├── models.py           # Added SEO methods
│   │   ├── views.py            # Added robots_txt view
│   │   └── urls.py             # Updated routes
│   ├── config/
│   │   ├── settings.py         # Added django.contrib.sitemaps
│   │   └── urls.py             # Added sitemap & robots.txt routes
│   ├── templates/
│   │   ├── base.html           # Enhanced with meta tags
│   │   └── laptops/
│   │       └── laptop_detail.html  # Added Schema.org
│   └── static/
│       └── robots.txt          # Static robots.txt
├── deploy_seo.bat              # Setup script
├── test_seo.py                 # Test script
├── SEO_GUIDE.md                # Comprehensive guide
└── SEO_QUICKSTART.md           # This file
```

## Google Search Console Setup

### 1. Verify Site Ownership
1. Go to [Google Search Console](https://search.google.com/search-console)
2. Add your property
3. Verify via HTML tag or DNS

### 2. Submit Sitemap
1. In Search Console, go to "Sitemaps"
2. Add sitemap URL: `https://yourdomain.com/sitemap.xml`
3. Wait for Google to crawl

### 3. Monitor Performance
- Check "Coverage" for indexing errors
- View "Performance" for search queries
- Fix any issues reported

## Validation Tools

### Google Rich Results Test
https://search.google.com/test/rich-results
- Test Product schema
- Check star ratings display
- Verify price & availability

### Facebook Sharing Debugger
https://developers.facebook.com/tools/debug/
- Test Open Graph tags
- Preview link appearance
- Refresh cached data

### Twitter Card Validator
https://cards-dev.twitter.com/validator
- Test Twitter Card rendering
- Preview card design

## Common Issues & Fixes

### Issue: Sitemap shows 404
**Fix:** Restart Django server after URL changes

### Issue: No structured data in Google test
**Fix:** Check if `{% load seo_tags %}` is at top of template

### Issue: Images not showing in social previews
**Fix:** 
1. Add actual images to static/
2. Update URLs in base.html
3. Use absolute URLs (including domain)

### Issue: Robots.txt not found
**Fix:** Check `robots_txt` view is imported in urls.py

## Next Steps

1. ✅ Deploy SEO features: `deploy_seo.bat`
2. ✅ Test locally: Visit sitemap.xml and robots.txt
3. ✅ Check page source for meta tags
4. ⬜ Add logo.png to static/
5. ⬜ Add og-image.jpg (1200x630) to static/
6. ⬜ Update domain in robots.txt for production
7. ⬜ Submit sitemap to Google Search Console
8. ⬜ Test with Google Rich Results

## Support

For detailed documentation, see **SEO_GUIDE.md**

For implementation details, check:
- `laptops/models.py` - SEO methods
- `laptops/sitemaps.py` - Sitemap config
- `templates/base.html` - Meta tags
- `laptops/templatetags/seo_tags.py` - Template tags
