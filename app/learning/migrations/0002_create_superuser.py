import os

from django.contrib.auth.hashers import make_password
from django.db import migrations


def forwards_func(apps, schema_editor):
    password = make_password(os.environ.get('ADMIN_PASSWORD', 'admin'))
    User = apps.get_model("learning", "User")
    user = User(username='admin', password=password, is_superuser=True, is_staff=True)
    user.save()


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
