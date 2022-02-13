# Generated by Django 3.2.5 on 2022-02-13 05:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20220212_1825'),
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('state', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='city',
            name='city',
            field=models.CharField(default='تهران', max_length=50, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='city',
            name='city_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='learncategory',
            name='category',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='learncategory',
            name='category_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='pricerange',
            name='price_range',
            field=models.CharField(max_length=50, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='pricerange',
            name='price_range_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='syllabus',
            name='syllabus',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='syllabus',
            name='syllabus_name',
            field=models.CharField(max_length=50),
        ),
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.AddField(
            model_name='teacher',
            name='state',
            field=models.ForeignKey(default='تهران', on_delete=django.db.models.deletion.CASCADE, to='accounts.state'),
        ),
    ]