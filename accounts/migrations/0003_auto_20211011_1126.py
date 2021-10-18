# Generated by Django 3.2.5 on 2021-10-11 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_city_learncategory_myuser_pricerange_student_syllabus_teacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='phone_number',
            field=models.CharField(max_length=13, unique=True, verbose_name='شماره همراه'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='experience',
            field=models.CharField(blank=True, default='3', max_length=3),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='national_id',
            field=models.PositiveIntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='qualification',
            field=models.CharField(blank=True, help_text='مدرک تحصیلی و گرایش تحصیلی خود را ذکر کنید', max_length=256),
        ),
    ]