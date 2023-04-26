from django.db import models
from django.urls import reverse
from django_resized import ResizedImageField
from django_unique_slugify import unique_slugify


class Blog(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(blank=True, null=True, allow_unicode=True)

    image1 = ResizedImageField( upload_to="blog/images/", size=[1300, 1300])
    image2 = ResizedImageField( upload_to="blog/images/", size=[1300, 1300])
    image3 = ResizedImageField( upload_to="blog/images/", size=[1300, 1300])
    image4 = ResizedImageField( upload_to="blog/images/", size=[1300, 1300])

    persian_main_title = models.CharField(max_length=200)
    persian_title1 = models.CharField(max_length=200)
    persian_title2 = models.CharField(max_length=200)
    persian_title3 = models.CharField(max_length=200)
    persian_title4 = models.CharField(max_length=200)

    text1 = models.TextField()
    text2 = models.TextField()
    text3 = models.TextField()
    text4 = models.TextField()


    def __str__(self):
        return f"{self.slug}"

    def get_absolute_url(self):
        return reverse('blog:named_blog_view',
                       args=[self.slug, ])

    def save(self, *args, **kwargs):
        unique_slugify(self, self.title)
        super(Blog, self).save(*args, **kwargs)
