from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator
from django.db import models
from django.urls import reverse
from django_resized import ResizedImageField
from django_unique_slugify import unique_slugify
from social_core.utils import slugify

from accounts.validators import validate_video_size, validate_image_size


class MyUser(AbstractUser):
    username = models.CharField(
        verbose_name='شماره همراه',
        max_length=50, blank=True,
        unique=True,
        help_text=None,
        validators=[],
        error_messages={
            'unique': "یک کاربر با این شماره موبایل وجود دارد لطفا از شماره دیگری استفاده کنید",
        },
    )



class City(models.Model):
    city = models.CharField(primary_key=True, max_length=50, default='تهران', unique=True)
    city_name = models.CharField(max_length=50, )

    def __str__(self):
        return self.city_name


class Syllabus(models.Model):
    syllabus = models.CharField(primary_key=True, max_length=50, )
    syllabus_name = models.CharField(max_length=50, )

    def __str__(self):
        return self.syllabus_name


class PriceRange(models.Model):
    price_range = models.IntegerField(primary_key=True, unique=True, default=150)
    price_range_name = models.CharField(max_length=50, )

    def __str__(self):
        return self.price_range_name


class Teacher(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE, )
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    national_id = models.PositiveIntegerField(blank=True, null=True)
    video_channel_link = models.URLField(blank=True, null=True)
    city = models.ForeignKey('City', on_delete=models.CASCADE, default='تهران')
    syllabus = models.ForeignKey('Syllabus', on_delete=models.CASCADE, )
    image = ResizedImageField(verbose_name='عکس استاد', upload_to='images/', validators=[],
                              size=[1200, 1200])
    degree_image = ResizedImageField(verbose_name='نمونه کار1', upload_to="images/", validators=[],
                                     size=[1300, 1300])
    degree_image2 = ResizedImageField(verbose_name='نمونه کار2 ', upload_to="images/", validators=[],
                                      size=[1300, 1300])
    degree_image3 = ResizedImageField(verbose_name='نمونه کار3', upload_to="images/", validators=[],
                                      size=[1300, 1300])
    degree_image4 = ResizedImageField(verbose_name='نمونه کار4', upload_to="images/", validators=[],
                                      size=[1300, 1300])
    degree_image5 = ResizedImageField(verbose_name='نمونه کار5', upload_to="images/", validators=[],
                                      size=[1300, 1300])
    degree_image6 = ResizedImageField(verbose_name='نمونه کار6', upload_to="images/", validators=[],
                                      size=[1300, 1300])
    degree_image7 = ResizedImageField(verbose_name='نمونه کار7', upload_to="images/", validators=[],
                                      size=[1300, 1300])
    degree_image8 = ResizedImageField(verbose_name='نمونه کار8', upload_to="images/", validators=[],
                                      size=[1300, 1300])
    work_image = ResizedImageField(verbose_name='عکس بازار کار', upload_to="images/", validators=[],
                                      size=[1300, 1300])
    debugging_image = ResizedImageField(verbose_name='عکس رفع اشکال', upload_to="images/", validators=[],
                                       size=[1300, 1300])
    friendly_image = ResizedImageField(verbose_name=' عکس دوستانه', upload_to="images/", validators=[],
                                       size=[1300, 1300])
    original_diploma_image = ResizedImageField(verbose_name=' عکس مدرک هنرجوها', upload_to="images/", validators=[],
                                       size=[1300, 1300])
    certificate_image1 = ResizedImageField(verbose_name='عکس مدرک استاد1', upload_to="images/",
                                           validators=[], size=[1300, 1300])
    certificate_image2 = ResizedImageField(verbose_name='عکس مدرک استاد2', upload_to="images/",
                                           validators=[], size=[1300, 1300])
    end_image = ResizedImageField(verbose_name='عکس پایانی', upload_to="images/",
                                           validators=[], size=[1300, 1300])

    workshop_number = models.CharField(max_length=100, blank=True, null=True)
    workshop_detail = models.CharField(max_length=100, blank=True, null=True)
    workshop_price = models.CharField(max_length=100, blank=True, null=True)
    qualification = models.TextField(max_length=1000, blank=True, null=True)
    experience = models.CharField(max_length=3, default='6', blank=True, null=True)
    points = models.FloatField(default=3.0, blank=True, null=True)
    sample_video = models.FileField(verbose_name='ویدیوی نمونه', upload_to='videos/', blank=True, null=True,
                                    validators=[FileExtensionValidator(allowed_extensions=['mp4', 'wmv', 'mov', '3gp']),
                                                validate_video_size], )
    describe_video = models.FileField(verbose_name='ویدیوی توضیح درباره خود و دوره', upload_to='videos/', blank=True,
                                      null=True,validators=[FileExtensionValidator(
                                          allowed_extensions=['mp4', 'wmv', 'mov', '3gp']), validate_video_size], )
    is_confirmed = models.BooleanField(default=False)
    slug = models.SlugField(blank=True, null=True, allow_unicode=True)
    users_like = models.ManyToManyField(MyUser, related_name='teachers_liked', blank=True)
    users_dislike = models.ManyToManyField(MyUser, related_name='teachers_disliked', blank=True)
    comment_num = models.IntegerField(default=0, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f"uid:{self.id}/{self.last_name}/{self.user.username}/{self.syllabus}"

    def get_absolute_url(self):
        return reverse('teachme:teacher_detail',
                       args=[ self.slug, ])

    def save(self, *args, **kwargs):
        unique_slugify(self, self.syllabus)
        super(Teacher, self).save(*args, **kwargs)


class Comment(models.Model):
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE, )
    user_commenter = models.ForeignKey('MyUser', on_delete=models.CASCADE, )
    name = models.CharField(max_length=100, null=True, blank=True)
    content = models.TextField(max_length=500, null=True, blank=True)
    is_confirmed = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.content:
            if self.is_confirmed:
                self.teacher.comment_num += 1
                self.teacher.save()
            super(Comment, self).save(*args, **kwargs)

    def __str__(self):
        return f"teacher:{self.teacher},commenter:{self.user_commenter}"


class ClassRequest(models.Model):
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE)
    student = models.ForeignKey('MyUser', on_delete=models.CASCADE)
    is_confirmed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    request_time = models.DateTimeField(auto_now=True, )

    def __str__(self):
        return f"teacher:{self.teacher.last_name}/uid:{self.teacher.user_id} - stu:{self.student}"
