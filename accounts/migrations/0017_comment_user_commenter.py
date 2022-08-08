# Generated by Django 3.2.5 on 2022-08-07 17:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='user_commenter',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='accounts.myuser'),
            preserve_default=False,
        ),
    ]
