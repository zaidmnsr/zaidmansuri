# Generated by Django 4.2 on 2023-07-29 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article_app', '0003_article_writer_alloted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='sub_keywords',
            field=models.TextField(blank=True, max_length=20000, null=True),
        ),
    ]
