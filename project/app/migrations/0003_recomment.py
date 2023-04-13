# Generated by Django 4.2 on 2023-04-13 06:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recomment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recomments', to='app.comment')),
            ],
        ),
    ]
