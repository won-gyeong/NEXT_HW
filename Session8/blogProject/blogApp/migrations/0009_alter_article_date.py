# Generated by Django 4.2 on 2023-04-06 08:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0008_alter_article_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 6, 8, 26, 52, 477503, tzinfo=datetime.timezone.utc)),
        ),
    ]
