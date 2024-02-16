# Generated by Django 4.2.10 on 2024-02-15 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_image_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='description',
            field=models.TextField(blank=True, help_text='Enter the image description. Max 1024 characters. Optional.', max_length=1024, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='image',
            name='title',
            field=models.CharField(help_text='Enter the image title.', max_length=128, verbose_name='Title'),
        ),
    ]
