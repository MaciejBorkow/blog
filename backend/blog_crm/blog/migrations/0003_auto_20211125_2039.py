# Generated by Django 3.1.3 on 2021-11-25 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20201221_0802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='articles',
            field=models.ManyToManyField(related_name='tags', to='blog.Article'),
        ),
    ]