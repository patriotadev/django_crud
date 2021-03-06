# Generated by Django 3.2.9 on 2021-12-13 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='todoData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Title')),
                ('done', models.BooleanField(blank=True, null=True, verbose_name='Done')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
