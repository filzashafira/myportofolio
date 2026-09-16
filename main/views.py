from django.shortcuts import render

from main.models import Experience
from .models import Education
from .models import Project
from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.shortcuts import render, redirect
from django.contrib import messages
from main.forms import ProjectForm


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

...

def create_project(request):
    form = ProjectForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Proyek baru berhasil ditambahkan!")
        return redirect("main:show_projects")

    context = {
        "name": "Filza",
        "form": form,
    }
    return render(request, "projects_form.html", context)

def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.all()

    if title_query:
        projects = projects.filter(title__icontains=title_query)

    projects_json = serializers.serialize("json", projects)
    return HttpResponse(projects_json, content_type="application/json")

def show_projects(request):
    json_response = get_projects_json(request)

    projects = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    projects = [project.object for project in projects]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Filza",
        "project_list": projects,
        "title_query": title_query,
    }
    return render(request, "project.html", context)

def delete_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        project.delete()
        messages.success(request, "Project berhasil dihapus!")
        return redirect("main:show_projects")

    return redirect("main:show_projects")
