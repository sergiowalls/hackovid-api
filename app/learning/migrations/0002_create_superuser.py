import os

from django.db import migrations


def forwards_func(apps, schema_editor):
    User = apps.get_model("learning", "User")
    User.objects.create_superuser(username='admin', password=os.environ.get('ADMIN_PASSWORD', 'admin'))


def reverse_func(apps, schema_editor):
    User = apps.get_model("learning", "User")
    User.objects.get(username='admin').delete()


class Migration(migrations.Migration):
    dependencies = [
        ('learning', '0001_initial'),
    ]
    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]
