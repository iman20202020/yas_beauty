# Generated by Django 3.2.5 on 2022-02-01 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_teacher_qualification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='national_id',
            field=models.PositiveIntegerField(blank=True),
        ),
    ]
