# Generated by Django 3.0.5 on 2020-04-11 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0002_create_superuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='saved_sections',
            field=models.ManyToManyField(blank=True, to='learning.Section'),
        ),
    ]
