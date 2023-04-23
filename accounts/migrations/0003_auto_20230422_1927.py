# Generated by Django 3.2.5 on 2023-04-22 14:57

import accounts.validators
from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20230422_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='certificate_image1',
            field=django_resized.forms.ResizedImageField(crop=None, default='img', force_format=None, keep_meta=True, quality=-1, scale=None, size=[300, 300], upload_to='images/', validators=[accounts.validators.validate_image_size], verbose_name='عکس مدرک استاد1'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='teacher',
            name='certificate_image2',
            field=django_resized.forms.ResizedImageField(crop=None, default='img', force_format=None, keep_meta=True, quality=-1, scale=None, size=[300, 300], upload_to='images/', validators=[accounts.validators.validate_image_size], verbose_name='عکس مدرک استاد2'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='teacher',
            name='degree_image',
            field=django_resized.forms.ResizedImageField(crop=None, default='img', force_format=None, keep_meta=True, quality=-1, scale=None, size=[300, 300], upload_to='images/', validators=[accounts.validators.validate_image_size], verbose_name='نمونه کار1'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='teacher',
            name='degree_image10',
            field=django_resized.forms.ResizedImageField(crop=None, default='img', force_format=None, keep_meta=True, quality=-1, scale=None, size=[300, 300], upload_to='images/', validators=[accounts.validators.validate_image_size], verbose_name='نمونه کار10'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='teacher',
            name='degree_image11',
            field=django_resized.forms.ResizedImageField(crop=None, default='img', force_format=None, keep_meta=True, quality=-1, scale=None, size=[300, 300], upload_to='images/', validators=[accounts.validators.validate_image_size], verbose_name='نمونه کار11'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='teacher',
            name='degree_image12',
            field=django_resized.forms.ResizedImageField(crop=None, default='img', force_format=None, keep_meta=True, quality=-1, scale=None, size=[300, 300], upload_to='images/', validators=[accounts.validators.validate_image_size], verbose_name='نمونه کار12'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='teacher',
            name='degree_image2',
            field=django_resized.forms.ResizedImageField(crop=None, default='img', force_format=None, keep_meta=True, quality=-1, scale=None, size=[300, 300], upload_to='images/', validators=[accounts.validators.validate_image_size], verbose_name='نمونه کار2 '),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='teacher',
            name='degree_image3',
            field=django_resized.forms.ResizedImageField(crop=None, default='img', force_format=None, keep_meta=True, quality=-1, scale=None, size=[300, 300], upload_to='images/', validators=[accounts.validators.validate_image_size], verbose_name='نمونه کار3'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='teacher',
            name='degree_image4',
            field=django_resized.forms.ResizedImageField(crop=None, default='img', force_format=None, keep_meta=True, quality=-1, scale=None, size=[300, 300], upload_to='images/', validators=[accounts.validators.validate_image_size], verbose_name='نمونه کار4'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='teacher',
            name='degree_image5',
            field=django_resized.forms.ResizedImageField(crop=None, default='img', force_format=None, keep_meta=True, quality=-1, scale=None, size=[300, 300], upload_to='images/', validators=[accounts.validators.validate_image_size], verbose_name='نمونه کار5'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='teacher',
            name='degree_image6',
            field=django_resized.forms.ResizedImageField(crop=None, default='img', force_format=None, keep_meta=True, quality=-1, scale=None, size=[300, 300], upload_to='images/', validators=[accounts.validators.validate_image_size], verbose_name='نمونه کار6'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='teacher',
            name='degree_image7',
            field=django_resized.forms.ResizedImageField(crop=None, default='img', force_format=None, keep_meta=True, quality=-1, scale=None, size=[300, 300], upload_to='images/', validators=[accounts.validators.validate_image_size], verbose_name='نمونه کار7'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='teacher',
            name='degree_image8',
            field=django_resized.forms.ResizedImageField(crop=None, default='img', force_format=None, keep_meta=True, quality=-1, scale=None, size=[300, 300], upload_to='images/', validators=[accounts.validators.validate_image_size], verbose_name='نمونه کار8'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='teacher',
            name='degree_image9',
            field=django_resized.forms.ResizedImageField(crop=None, default='img', force_format=None, keep_meta=True, quality=-1, scale=None, size=[300, 300], upload_to='images/', validators=[accounts.validators.validate_image_size], verbose_name='نمونه کار9'),
            preserve_default=False,
        ),
    ]
