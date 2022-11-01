import os

from django.contrib.auth.base_user import AbstractBaseUser
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator
from django.db import models
from django.urls import reverse
from django_resized import ResizedImageField
from accounts.validators import validate_video_size, validate_image_size


class MyUser(AbstractUser):
    username = models.CharField(
        verbose_name='شماره همراه',
        max_length=50,blank=True,
        unique=True,
        help_text=None,
        validators=[],

        error_messages={
            'unique': "یک کاربر با این شماره موبایل وجود دارد لطفا از شماره دیگری استفاده کنید",
        },
    )


class State(models.Model):
    state = models.CharField(primary_key=True, max_length=50,unique=True)

    def __str__(self):
        return self.state


class City(models.Model):
    state = models.ForeignKey('State', on_delete=models.CASCADE)
    city = models.CharField(primary_key=True, max_length=50, default='تهران', unique=True)
    city_name = models.CharField(max_length=50, )

    def __str__(self):
        return self.city_name


class LearnCategory(models.Model):
    category = models.CharField(primary_key=True, max_length=50, )
    category_name = models.CharField(max_length=50, )

    def __str__(self):
        return self.category_name


class Syllabus(models.Model):
    learn_category = models.ForeignKey('LearnCategory', on_delete=models.CASCADE)
    syllabus = models.CharField(primary_key=True, max_length=50, )
    syllabus_name = models.CharField(max_length=50, )

    def __str__(self):
        return self.syllabus_name


class PriceRange(models.Model):
    price_range = models.IntegerField(primary_key=True, unique=True,default=150)
    price_range_name = models.CharField(max_length=50,)

    def __str__(self):
        return self.price_range_name


class Teacher(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE, )
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    national_id = models.PositiveIntegerField(blank=True, null=True)
    price_range = models.ForeignKey('PriceRange', on_delete=models.CASCADE,)
    video_channel_link = models.URLField(blank=True, null=True)
    state = models.ForeignKey('State', on_delete=models.CASCADE, default='تهران')
    city = models.ForeignKey('City', on_delete=models.CASCADE, default='تهران')
    category = models.ForeignKey('LearnCategory', on_delete=models.CASCADE,)
    syllabus = models.ForeignKey('Syllabus', on_delete=models.CASCADE, )
    image = ResizedImageField(upload_to='images/', blank=True,validators=[validate_image_size], size=[300,300])
    # national_card_image = ResizedImageField(upload_to='images/',blank=True,validators=[validate_image_size],null=True)
    degree_image = ResizedImageField(upload_to="images/", validators=[validate_image_size],blank=True,null=True, size=[300,300])
    degree_image2 = ResizedImageField(upload_to="images/", validators=[validate_image_size],blank=True,null=True, size=[300,300])
    degree_image3 = ResizedImageField(upload_to="images/", validators=[validate_image_size],blank=True,null=True, size=[300,300])
    degree_image4 = ResizedImageField(upload_to="images/", validators=[validate_image_size],blank=True,null=True, size=[300,300])
    degree_image5 = ResizedImageField(upload_to="images/", validators=[validate_image_size],blank=True,null=True, size=[300,300])
    degree_image6 = ResizedImageField(upload_to="images/", validators=[validate_image_size],blank=True,null=True, size=[300,300])
    degree_image7 = ResizedImageField(upload_to="images/", validators=[validate_image_size],blank=True,null=True, size=[300,300])
    # jozveh = models.FileField(upload_to="jozveh/", blank=True,)
    workshop_number =models.CharField(max_length=100, blank=True)
    workshop_detail = models.CharField(max_length=100, blank=True)
    workshop_price = models.CharField(max_length=100, blank=True)
    qualification = models.TextField(max_length=1000,blank=True,)
    experience = models.CharField(max_length=3, default='6', blank=True)
    points = models.FloatField(default=3.0, blank=True)
    sample_video = models.FileField(verbose_name='ویدیوی نمونه',upload_to='videos/',blank=True,
          validators=[FileExtensionValidator( allowed_extensions=['mp4', 'wmv','mov','3gp']),validate_video_size],)
    learn_type = models.IntegerField(default=0,blank=True)
    is_confirmed = models.BooleanField(default=False)
    gender = models.IntegerField(default=1,blank=True)
    slug = models.SlugField(blank=True,null=True , allow_unicode=True)
    users_like = models.ManyToManyField(MyUser, related_name='teachers_liked', blank=True)
    users_dislike = models.ManyToManyField(MyUser, related_name='teachers_disliked', blank=True)
    comment_num = models.IntegerField(default=0, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f"uid:{self.user_id}/{self.last_name}/{self.user.username}/{self.syllabus}"


    def get_absolute_url(self):
        return reverse('teachme:teacher_detail',
                       args=[self.id, self.slug])
    #
    def save(self, *args, **kwargs):
        slug1 = str(self.syllabus).replace(" ", "-")
        self.slug = slug1
        # image_rename(self)
        super(Teacher, self).save(*args, **kwargs)


class Comment(models.Model):
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE, )
    user_commenter = models.ForeignKey('MyUser',on_delete=models.CASCADE, )
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
    request_time = models.DateTimeField(auto_now=True,)

    def __str__(self):
        return f"teacher:{self.teacher.last_name}/uid:{self.teacher.user_id} - stu:{self.student}"



