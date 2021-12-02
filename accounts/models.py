
from django.contrib.auth.base_user import AbstractBaseUser
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator, EmailValidator, validate_email
from django.db import models


from accounts.validators import validate_video_size, validate_image_size


class MyUser(AbstractUser):
    phone_number = models.CharField(verbose_name='شماره همراه',max_length=13,blank=False,unique=True,)


    username = models.CharField(
        verbose_name="ایمیل",
        max_length=50,
        unique=True,
        help_text=None,
        validators=[validate_email],
        error_messages={
            'unique':"یک کاربر با این ایمیل وجود دارد .",
        },
    )
class City(models.Model):
    city = models.CharField(primary_key=True, max_length=15, default='تهران', unique=True)
    city_name = models.CharField(max_length=30, )
    def __str__(self):
        return self.city_name


class LearnCategory(models.Model):
    category = models.CharField(primary_key=True, max_length=15, )
    category_name = models.CharField(max_length=30, )

    def __str__(self):
        return self.category_name


class Syllabus(models.Model):
    learn_category = models.ForeignKey('LearnCategory', on_delete=models.CASCADE)
    syllabus = models.CharField(primary_key=True, max_length=15, )
    syllabus_name = models.CharField(max_length=20, )

    def __str__(self):
        return self.syllabus_name


class PriceRange(models.Model):
    price_range = models.CharField(primary_key=True, max_length=10,  unique=True)
    price_range_name = models.CharField(max_length=30,)

    def __str__(self):
        return self.price_range_name


class Teacher(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE, )
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    national_id = models.PositiveIntegerField(unique=True)
    price_range = models.ForeignKey('PriceRange', on_delete=models.CASCADE)
    # language = models.ForeignKey('Language', on_delete=models.CASCADE)
    city = models.ForeignKey('City', on_delete=models.CASCADE, default='تهران')
    syllabus = models.ForeignKey('Syllabus', on_delete=models.CASCADE, )
    category = models.ForeignKey('LearnCategory', on_delete=models.CASCADE, default='uni')
    image = models.ImageField(upload_to='images/', blank=True,validators=[validate_image_size])
    national_card_image = models.ImageField(upload_to='images/',blank=True,validators=[validate_image_size],
                                            help_text='عکس خود را اینجا بارگذاری کنید')
    degree_image = models.ImageField(upload_to="images/", validators=[validate_image_size],blank=True,
                                     help_text='عکس مدرک تحصیلی خود را بارگذاری کنید')
    qualification = models.CharField(max_length=120,blank=True, help_text='مدرک تحصیلی و گرایش تحصیلی خود را ذکر کنید')
    experience = models.CharField(max_length=3, default='3', blank=True)
    points = models.IntegerField(default=3, blank=True)
    sample_video = models.FileField(verbose_name='ویدیوی نمونه',upload_to='videos/',blank=True,
                                    validators=[FileExtensionValidator(
                                        allowed_extensions=['mp4', 'wmv','mov','3gp'])
                                        ,validate_video_size],
                                    help_text='یک ویدیو حداکثر سه دقیقه از تدریس خود بارگذاری کنید')
    learn_type = models.IntegerField( default=0,blank=True)
    is_confirmed = models.BooleanField(default=False)
    gender = models.IntegerField(default=1,blank=True)

    def __str__(self):
        return self.last_name+","+self.user.phone_number

class Student(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE, blank=True)
    price_range = models.ForeignKey('PriceRange', on_delete=models.CASCADE)
    learn_type = models.IntegerField(blank=True,default=0)
    syllabus = models.ForeignKey('Syllabus', on_delete=models.CASCADE, default='phys')
    category = models.ForeignKey('LearnCategory', on_delete=models.CASCADE, default='uni')
    city = models.ForeignKey('City', on_delete=models.CASCADE, default='تهران')


class StudentSubmit(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE,blank=True)
    first_name = models.CharField(verbose_name='نام', max_length=30)
    last_name = models.CharField(verbose_name='نام خانوادگی', max_length=30)
    national_id = models.PositiveIntegerField(unique=True)

    gender = models.IntegerField(default=1, blank=True,  verbose_name='جنسیت')

    def __str__(self):
        return self.last_name+','+self.user.phone_number

class RequestClass(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE,blank=True)
    student = models.ForeignKey(StudentSubmit, on_delete=models.CASCADE,blank=True)
    start_date = models.DateField(auto_now_add=True)
    is_confirmed = models.BooleanField(default=False)
    is_started = models.BooleanField(default=False)
    number_of_sessions = models.PositiveIntegerField(blank=True,null=True)
    price = models.PositiveIntegerField(blank=True,null=True)
    class_type_choices = (
        ('حضوری', 'حضوری'),
        ('آنلاین', 'آنلاین'),
        ('حضوری و آنلاین', 'حضوری و آنلاین'),
                       )
    type_of_class = models.CharField(max_length=20,choices=class_type_choices,default='حضوری')

    def __str__(self):
        return "t:"+self.teacher.user.phone_number+" ,s: "+self.student.user.phone_number
