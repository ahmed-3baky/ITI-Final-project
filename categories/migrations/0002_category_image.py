# Generated by Django 5.0.6 on 2024-09-06 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, default='default/default.jpg', null=True, upload_to='project_images/'),
        ),
    ]
