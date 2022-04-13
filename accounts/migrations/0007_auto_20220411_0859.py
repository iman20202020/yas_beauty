# Generated by Django 3.2.5 on 2022-04-11 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_remove_teacher_first_free'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricerange',
            name='price_range',
            field=models.IntegerField(default=150, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='qualification',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
