# Generated by Django 4.1.2 on 2022-10-11 07:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='images/')),
                ('fee', models.PositiveIntegerField()),
                ('duration', models.CharField(max_length=200)),
                ('students', models.PositiveIntegerField()),
                ('start', models.CharField(max_length=200)),
                ('method', models.CharField(max_length=200)),
                ('entry_requirements', models.CharField(max_length=200)),
                ('exam_body', models.CharField(max_length=200)),
                ('other_requirements', models.TextField(blank=True, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.category')),
            ],
        ),
    ]
