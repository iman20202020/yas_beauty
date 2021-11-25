# Generated by Django 3.2.5 on 2021-11-25 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_teacher_degree_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(auto_now_add=True)),
                ('student', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.studentsubmit')),
                ('teacher', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.teacher')),
            ],
        ),
    ]
