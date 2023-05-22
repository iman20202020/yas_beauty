from django.contrib.sitemaps import Sitemap
from .models import Teacher

class TeacherSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Teacher.objects.all()

    def lastmod(self, obj):
        return obj.updated

