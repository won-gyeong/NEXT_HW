# Generated by Django 4.2 on 2023-04-05 08:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0006_alter_article_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 5, 8, 58, 11, 812008, tzinfo=datetime.timezone.utc)),
        ),
    ]
