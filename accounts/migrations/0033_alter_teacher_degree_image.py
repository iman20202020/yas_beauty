# Generated by Django 3.2.5 on 2022-08-15 20:27

import accounts.validators
from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0032_alter_teacher_degree_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='degree_image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=-1, scale=None, size=[300, 300], upload_to='images/', validators=[accounts.validators.validate_image_size]),
        ),
    ]