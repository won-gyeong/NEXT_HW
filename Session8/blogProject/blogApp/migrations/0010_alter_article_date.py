# Generated by Django 4.2 on 2023-04-06 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0009_alter_article_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
