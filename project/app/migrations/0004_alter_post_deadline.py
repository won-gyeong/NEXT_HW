# Generated by Django 4.2 on 2023-04-09 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_post_end_date_post_deadline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='deadline',
            field=models.DateField(null=True),
        ),
    ]
