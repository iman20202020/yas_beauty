# Generated by Django 3.2.5 on 2022-04-06 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_pricerange_price_range'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='first_free',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
