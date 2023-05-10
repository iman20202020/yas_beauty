from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django_resized import ResizedImageField
from django_unique_slugify import unique_slugify

from blog.page_creator import page_create


class Blog(models.Model):
    title = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(blank=True, null=True, allow_unicode=True)

    image1 = ResizedImageField( upload_to="blog/images/", size=[800, 800])
    image2 = ResizedImageField( upload_to="blog/images/", size=[800, 800], null=True, blank=True)
    image3 = ResizedImageField( upload_to="blog/images/", size=[800, 800], null=True, blank=True)
    image4 = ResizedImageField( upload_to="blog/images/", size=[800, 800], null=True, blank=True)

    persian_main_title = models.CharField(max_length=200)
    persian_title1 = models.CharField(max_length=200, null=True, blank=True)
    persian_title2 = models.CharField(max_length=200, null=True, blank=True)
    persian_title3 = models.CharField(max_length=200, null=True, blank=True)
    persian_title4 = models.CharField(max_length=200, null=True, blank=True)

    text1 = models.TextField()
    text2 = models.TextField(null=True, blank=True)
    text3 = models.TextField(null=True, blank=True)
    text4 = models.TextField(null=True, blank=True)
    publish = models.BooleanField(default=True)


    def __str__(self):
        return f"{self.slug}"

    def get_absolute_url(self):
        return reverse('blog:named_blog_view',
                       args=[self.slug, ])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        page_create(self)
        super(Blog, self).save(*args, **kwargs)
