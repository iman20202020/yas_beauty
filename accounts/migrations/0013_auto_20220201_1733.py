# Generated by Django 3.2.5 on 2022-02-01 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_auto_20220201_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='learncategory',
            name='category_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='syllabus',
            name='syllabus_name',
            field=models.CharField(max_length=20),
        ),
    ]
