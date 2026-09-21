from django.forms import ModelForm, TextInput, Textarea, URLInput

from main.models import Project
from main.models import Award

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
            "tech_stack": "Kategori / Topik / Metode",
            "project_url": "URL Proyek",
            "project_image_url": "URL Gambar Proyek",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "KTI, Eco Enzyme, SDGs, Research",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Ceritakan Proyekmu",
                    "rows": 3,
                }
            ),
            "tech_stack": TextInput(
                attrs={
                    "placeholder": "Django, Python, HTML, CSS, KTI",
                }
            ),
            "project_url": URLInput(
                attrs={
                    "placeholder": "https://github.com/filzashafira/myportofolio",
                }
            ),
            "project_image_url": URLInput(
                attrs={
                    "placeholder": "https://drive.google.com/thumbnail?id=FILE_ID&sz=w1000",

                }
            ),
        }


class AwardForm(ModelForm):
    class Meta:
        model = Award
        fields = [
            "title",
            "description",
            "tech_stack",
            "award_url",
            "award_image_url",
        ]

        labels = {
            "title": "Nama Prestasi",
            "description": "Deskripsi Penghargaan",
            "award_url": "URL Proyek",
            "award_image_url": "URL Gambar Penghargaan",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Business plan ",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Ceritakan Prestasimu",
                    "rows": 3,
                }
            ),
            "awards_url": URLInput(
                attrs={
                    "placeholder": "https://drive.google.com/thumbnail?id=FILE_ID&sz=w1000",
                }
            ),
            "awards_image_url": URLInput(
                attrs={
                    "placeholder": "https://drive.google.com/thumbnail?id=FILE_ID&sz=w1000",
                }
            ),
        }