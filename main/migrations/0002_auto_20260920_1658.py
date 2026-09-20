from django.db import migrations

def create_pws_superuser(apps, schema_editor):
    from django.contrib.auth import get_user_model
    User = get_user_model()
    
    username = 'filza'
    email = 'filza.shafira@ui.ac.id'
    password = 'bismillah.filza0707'  

    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username=username, email=email, password=password)

class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'), 
    ]

    operations = [
        migrations.RunPython(create_pws_superuser),
    ]