from django.forms import ModelForm, TextInput, Textarea, URLInput

from main.models import Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = [
            "title",
            "description",
            "tech_stack",
            "project_url",
            "project_image_url",
        ]

        labels = {
            "title": "Nama Proyek",
            "description": "Deskripsi Proyek",
            "tech_stack": "Teknologi yang Digunakan",
            "project_url": "URL Proyek",
            "project_image_url": "URL Gambar Proyek",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Portfolio Website",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Initiated ECO SMART (Effective and Careful with Eco Enzyme), an innovative solution transforming organic waste into eco-friendly soap to support the Sustainable Development Goals (SDGs). Led formulation testing and end-to-end production to deliver a practical, high-value product for waste reduction and community sustainability.",
                    "rows": 3,
                }
            ),
            "tech_stack": TextInput(
                attrs={
                    "placeholder": "Django, Python, HTML, CSS",
                }
            ),
            "project_url": URLInput(
                attrs={
                    "placeholder": "https://github.com/filzashafira/myportfolio",
                }
            ),
            "project_image_url": URLInput(
                attrs={
                    "placeholder": "https://cdn.phototourl.com/free/2026-09-16-698952c8-d5fb-48a8-9f09-ba6ac96d373f.png",
                }
            ),
        }