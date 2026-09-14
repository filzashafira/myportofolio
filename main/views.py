from django.shortcuts import render

from main.models import Experience
from .models import Education


def show_main(request):
    context = {
        "name": "Filza Shafira",
        "npm": "2506623641",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "A highly motivated and growth-minded individual with a deep curiosity in technology, science, and business. Known for strong public speaking skills, critical thinking, and a proactive mindset. I thrive in dynamic environments that  challenge me to learn, adapt, and contribute meaningfully. With a solid foundation in analytical thinking and  communication, I am eager to expand my capabilities and make a positive impact through both academic and real-world experiences."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Filza Shafira",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)

def show_education(request):
    education_list = Education.objects.all()
    context = {
        'name': 'Filza Shafira',
        'education_list': education_list,
    }
    return render(request, 'education.html', context)
