# Generated by Django 3.2.5 on 2023-03-26 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0004_auto_20230323_1152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, upload_to='imagenew'),
        ),
    ]