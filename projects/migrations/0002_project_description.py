# Generated by Django 5.1.2 on 2024-10-19 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='description',
            field=models.TextField(default='test'),
            preserve_default=False,
        ),
    ]
