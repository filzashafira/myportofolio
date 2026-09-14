import os
from django.db import migrations

def load_fixture(apps, schema_editor):
    from django.core.management import call_command
    fixture_path = os.path.join(os.path.dirname(__file__), '../../main_data.json')
    if os.path.exists(fixture_path):
        call_command('loaddata', fixture_path)

def reverse_load(apps, schema_editor):
    pass

class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),  # Sesuaikan dengan nama file migrasi pertama kamu
    ]

    operations = [
        migrations.RunPython(load_fixture, reverse_code=reverse_load),
    ]