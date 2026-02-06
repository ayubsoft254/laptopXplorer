"""
Management command to create a sample article
Usage: python manage.py create_sample_article
"""
from django.core.management.base import BaseCommand
from laptops.models import Laptop, Article

class Command(BaseCommand):
    help = 'Creates a sample article for the LaptopXplorer platform'

    def handle(self, *args, **kwargs):
        self.stdout.write("\n" + "="*60)
        self.stdout.write("Creating Sample Article")
        self.stdout.write("="*60 + "\n")

        # Find the MacBook Air M2
        try:
            laptop = Laptop.objects.get(name__icontains="MacBook Air", processor__name__icontains="M2")
        except Laptop.DoesNotExist:
            self.stdout.write(self.style.ERROR("MacBook Air M2 not found in database!"))
            self.stdout.write("Available laptops:")
            for lap in Laptop.objects.all()[:5]:
                self.stdout.write(f"  - {lap.name}")
            return
        except Laptop.MultipleObjectsReturned:
            laptop = Laptop.objects.filter(name__icontains="MacBook Air", processor__name__icontains="M2").first()

        # Article content
        article_content = """
<div class="article-content">
    <h2>A New Standard for Ultraportable Computing</h2>
    
    <p>The MacBook Air M2 represents Apple's boldest redesign of its most popular laptop in over a decade. Gone is the iconic wedge shape that defined the Air since 2008, replaced by a uniform, sleek chassis that wouldn't look out of place in a sci-fi movie. But this isn't just a cosmetic refresh—the M2 chip inside brings substantial performance improvements that blur the line between ultraportable and pro-level machines.</p>

    <h3>Design Evolution: Out with the Wedge, In with Minimalism</h3>
    
    <p>At first glance, the new Air looks remarkably similar to the 14-inch MacBook Pro. The tapered design is gone, replaced by a flat, uniform body that measures just 11.3mm thin throughout. It's actually slightly thicker at its thickest point than the old Air, but the consistency makes it feel more premium and modern.</p>

    <p>The weight is nearly identical to its predecessor at 2.7 pounds, making it effortlessly portable. I carried it daily for two weeks in a messenger bag, and there were moments I genuinely forgot it was there. The new Midnight color option is stunning, though it does show fingerprints more readily than the other finishes.</p>

    <h3>Display: Finally, a Notch Worth Having</h3>
    
    <p>The 13.6-inch Liquid Retina display is a massive upgrade. With 500 nits of brightness and support for one billion colors, content looks vibrant and punchy. The increased screen real estate comes from slimmer bezels and that controversial notch at the top—which houses an improved 1080p webcam that finally does justice to video calls.</p>

    <p>During testing, the display handled everything from photo editing in Lightroom to streaming HDR content on Apple TV+. While it lacks the ProMotion technology of the MacBook Pro line, the 60Hz refresh rate is perfectly adequate for the Air's target audience. Colors are accurate out of the box, and the anti-reflective coating works well even in bright office environments.</p>

    <h3>M2 Performance: Serious Power in a Fanless Design</h3>
    
    <p>The M2 chip is the real star here. Built on a 5-nanometer process, it packs 20 billion transistors—25% more than the M1. In real-world use, this translates to noticeably snappier performance across the board.</p>

    <p>I threw a variety of workloads at it: 4K video editing in Final Cut Pro, compiling code in Xcode, running multiple virtual machines, and the usual barrage of 50+ browser tabs. The Air handled everything without breaking a sweat. Export times for a 5-minute 4K video project were around 3 minutes—impressive for a fanless machine.</p>

    <p>The lack of a cooling fan means the Air is completely silent, even under heavy load. There's some thermal throttling during sustained workloads, but for 90% of users, you'll never notice. The base model with 8GB of RAM performed admirably, though I'd recommend the 16GB upgrade for anyone doing serious creative work or heavy multitasking.</p>

    <h3>Battery Life: All-Day Champion</h3>
    
    <p>Apple claims up to 18 hours of video playback, and while real-world usage is always lower, the Air delivers exceptional battery life. In my testing, with brightness at 50%, multiple apps running, and constant web browsing, I consistently got 12-14 hours of use.</p>

    <p>For lighter tasks like writing or web browsing, pushing past 16 hours is entirely feasible. The included MagSafe 3 charging port is a welcome return, freeing up one of the two Thunderbolt ports. Fast charging via the optional 67W adapter gets you to 50% in about 30 minutes.</p>

    <h3>The Keyboard and Audio Experience</h3>
    
    <p>The Magic Keyboard remains one of the best laptop keyboards on the market. The key travel is shallow but satisfying, and the layout is spacious. Touch typists will feel right at home. The full-height function row is a nice touch, replacing the half-height keys of the previous generation.</p>

    <p>Audio quality is surprisingly robust for such a thin machine. The four-speaker system with Spatial Audio support delivers clear mids and highs, though bass is understandably limited. It's more than adequate for video calls, YouTube, and casual music listening, but audiophiles will want external speakers or headphones.</p>

    <h3>Who Should Buy the MacBook Air M2?</h3>
    
    <p>The MacBook Air M2 is the perfect laptop for the vast majority of users. Students, professionals, creatives who don't need the horsepower of a MacBook Pro, and anyone who values portability without sacrificing performance will find this machine exceptional.</p>

    <p>At $1,199 for the base model, it's not cheap, but you're getting a premium build, class-leading battery life, a gorgeous display, and performance that rivals many more expensive Windows ultrabooks. If you're already in the Apple ecosystem, this is a no-brainer upgrade from any MacBook older than two years.</p>

    <h3>Final Verdict</h3>
    
    <p>The MacBook Air M2 is what the Air has always promised to be: a laptop that gets out of your way and lets you work anywhere, anytime. It's fast, beautiful, silent, and lasts all day. While the starting price has crept up and the base storage of 256GB feels stingy in 2024, these are minor quibbles in an otherwise outstanding package.</p>

    <p><strong>Rating: 9.5/10</strong></p>

    <h4>Pros:</h4>
    <ul>
        <li>Exceptional M2 performance in fanless design</li>
        <li>All-day battery life (12-16 hours real-world)</li>
        <li>Gorgeous 13.6" Liquid Retina display</li>
        <li>Premium build quality and design</li>
        <li>Completely silent operation</li>
        <li>Improved 1080p webcam</li>
    </ul>

    <h4>Cons:</h4>
    <ul>
        <li>Base 256GB storage feels limiting</li>
        <li>Only two Thunderbolt ports</li>
        <li>Midnight finish shows fingerprints</li>
        <li>No ProMotion display</li>
        <li>8GB base RAM could be limiting for power users</li>
    </ul>
</div>
"""

        # Create the article
        article, created = Article.objects.get_or_create(
            slug='macbook-air-m2-review-2024',
            defaults={
                'title': 'MacBook Air M2 Review: The Perfect Laptop for Almost Everyone',
                'laptop': laptop,
                'author_name': 'Sarah Mitchell',
                'author_bio': 'Sarah is a senior technology journalist with over 10 years of experience reviewing laptops and mobile devices. She specializes in ultraportable computing and has tested hundreds of laptops across all price ranges.',
                'excerpt': 'Apple\'s redesigned MacBook Air M2 combines stunning design with M2 chip performance in a fanless package. After two weeks of intensive testing, we explore whether this ultraportable powerhouse lives up to the hype and deserves its place as the default laptop recommendation for 2024.',
                'content': article_content.strip(),
                'read_time': 8,
                'published': True,
                'featured': True,
                'views': 1247,
                'likes': 89
            }
        )

        if created:
            self.stdout.write(self.style.SUCCESS(f"\n✅ Article created successfully!"))
            self.stdout.write(f"\nTitle: {article.title}")
            self.stdout.write(f"Slug: {article.slug}")
            self.stdout.write(f"Laptop: {article.laptop.name}")
            self.stdout.write(f"Author: {article.author_name}")
            self.stdout.write(f"Read Time: {article.read_time} min")
            self.stdout.write(f"Status: {'Published' if article.published else 'Draft'}")
            self.stdout.write(f"Featured: {'Yes' if article.featured else 'No'}")
            self.stdout.write(f"\n📝 View at: /laptops/article/{article.slug}/")
            self.stdout.write(f"🏠 Featured on homepage (Expert Articles section)")
        else:
            self.stdout.write(self.style.WARNING(f"\n⚠️  Article already exists: {article.title}"))

        self.stdout.write("\n" + "="*60)
        self.stdout.write("Done!")
        self.stdout.write("="*60 + "\n")
