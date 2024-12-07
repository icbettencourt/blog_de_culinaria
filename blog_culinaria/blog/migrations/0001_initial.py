# Generated by Django 5.0.6 on 2024-07-09 18:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='blog/')),
                ('ingredients', models.TextField()),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.category')),
            ],
        ),
    ]
