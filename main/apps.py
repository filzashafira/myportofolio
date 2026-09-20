from django.apps import AppConfig
import sys

class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'

    def ready(self):
        # Jalankan otomatis saat server/PWS berjalan
        if 'gunicorn' in sys.argv or 'wsgi' in sys.argv:
            from django.core.management import call_command
            from main.models import Experience
            
            try:
                # Cek jika data Experience di PWS masih kosong, isi otomatis dari file JSON
                if not Experience.objects.exists():
                    call_command('loaddata', 'experience.json')
            except Exception:
                pass

class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'

    def ready(self):
        # Jalankan otomatis saat aplikasi Django start di server PWS
        if 'gunicorn' in sys.argv or 'wsgi' in sys.argv:
            from django.core.management import call_command
            try:
                call_command('create_pws_superuser')
            except Exception:
                pass