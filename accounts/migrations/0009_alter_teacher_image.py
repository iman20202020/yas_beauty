# Generated by Django 3.2.5 on 2022-07-31 14:08

import accounts.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_teacher_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/', validators=[accounts.validators.validate_image_size]),
        ),
    ]