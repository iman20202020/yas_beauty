# Generated by Django 3.2.5 on 2023-05-06 09:36

from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blog_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image2',
            field=django_resized.forms.ResizedImageField(crop=None, force_format=None, keep_meta=True, null=True, quality=-1, scale=None, size=[800, 800], upload_to='blog/images/'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='image3',
            field=django_resized.forms.ResizedImageField(crop=None, force_format=None, keep_meta=True, null=True, quality=-1, scale=None, size=[800, 800], upload_to='blog/images/'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='image4',
            field=django_resized.forms.ResizedImageField(crop=None, force_format=None, keep_meta=True, null=True, quality=-1, scale=None, size=[800, 800], upload_to='blog/images/'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='persian_title1',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='persian_title2',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='persian_title3',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='persian_title4',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='text2',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='text3',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='text4',
            field=models.TextField(null=True),
        ),
    ]