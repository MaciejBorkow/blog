# Generated by Django 3.1.3 on 2020-11-30 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_change_article_file_field_to_path_field'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='background',
        ),
        migrations.AddField(
            model_name='article',
            name='background_uri',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
