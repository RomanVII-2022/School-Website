# Generated by Django 4.1.2 on 2022-10-13 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='staffprofile/'),
        ),
    ]
