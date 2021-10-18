# Generated by Django 3.2.5 on 2021-10-11 15:53

import accounts.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20211011_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='degree_image',
            field=models.ImageField(help_text='عکس مدرک تحصیلی خود را بارگذاری کنید', upload_to='images/', validators=[accounts.validators.validate_image_size]),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='sample_video',
            field=models.FileField(blank=True, help_text='یک ویدیو حداکثر سه دقیقه از تدریس خود بارگذاری کنید', upload_to='videos/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4', 'wmv']), accounts.validators.validate_video_size], verbose_name='ویدیوی نمونه تدریس'),
        ),
    ]