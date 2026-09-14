import uuid
from django.db import models

class Experience(models.Model):
    EXPERIENCE_CHOICES = [
        ('INTERNSHIP', 'Internship'),
        ('RESEARCH', 'Research'),
        ('VOLUNTEER', 'Volunteer'),
        ('PART_TIME', 'Part-Time'),
        ('FULL_TIME', 'Full-Time'),
        ('FREELANCE', 'Freelance'),
        ('ORGANIZATIONAL', 'Organizational'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=EXPERIENCE_CHOICES, default='FULL_TIME')
    thumbnail = models.URLField(blank=True, null=True)
    started_at = models.DateTimeField(auto_now_add=True)
    ended_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

    @property
    def is_ongoing(self):
        return self.ended_at is None


class Education(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    institution = models.CharField(max_length=255)  # Misal: Universitas Indonesia
    degree = models.CharField(max_length=255)       # Misal: S1 Ilmu Komputer
    description = models.TextField(blank=True, null=True)
    start_year = models.IntegerField()
    end_year = models.IntegerField(blank=True, null=True)
    is_current = models.BooleanField(default=False)
    thumbnail = models.URLField(blank=True, null=True) # Pakai URLField agar sama seperti Experience

    def __str__(self):
        return self.institution
    
    @property
    def is_ongoing(self):
        return self.end_year is None or self.is_current