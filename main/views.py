
from django.shortcuts import render, redirect
from main.models import Experience, Education, Project,  Award
from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
import datetime
from django.contrib.auth import login, logout
from django.shortcuts import get_object_or_404, redirect, render
from .forms import ProjectForm, AwardForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required 
from django.core.exceptions import PermissionDenied       
from django.shortcuts import render, redirect
from main.forms import ProjectForm
from .models import Project


def show_main(request):
    last_login = request.COOKIES.get('last_login', 'Belum ada sesi login / Cookie tidak ditemukan')
    context = {
        "name": "Filza",
        "npm": "2506623641",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "A highly motivated and growth-minded individual with a deep curiosity in technology, science, and business. Known for strong public speaking skills, critical thinking, and a proactive mindset. I thrive in dynamic environments that  challenge me to learn, adapt, and contribute meaningfully. With a solid foundation in analytical thinking and  communication, I am eager to expand my capabilities and make a positive impact through both academic and real-world experiences. "
        ),
        "last_login": last_login,
    }
    return render(request, "index.html", context)

def show_experience(request):
    context = {
        "name": "Filza",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)

def show_education(request):
    education_list = Education.objects.all().order_by('-start_year')
    context = {
        'name': 'Filza Shafira',
        'education_list': education_list,
    }
    return render(request, 'education.html', context)

def create_project(request):
    form = ProjectForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Proyek baru berhasil ditambahkan!")
        return redirect("main:show_projects")

    context = {
        "name": "Filza Shafira",
        "form": form,
    }
    return render(request, "projects_form.html", context)

def delete_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        project.delete()
        messages.success(request, "Project berhasil dihapus!")
        return redirect("main:show_projects")

    return redirect("main:show_projects")

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

@login_required(login_url="/login/")
def create_project(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    
    form = ProjectForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Proyek baru berhasil ditambahkan!")
        return redirect("main:show_projects")

    context = {
        "name": "Filza Shafira",
        "form": form,
    }
    return render(request, "projects_form.html", context)

def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.all()

    if title_query:
        projects = projects.filter(title__icontains=title_query)

    projects_json = serializers.serialize(
    "json", projects, use_natural_foreign_keys=True 
)
    return HttpResponse(projects_json, content_type="application/json")

@login_required(login_url="/login/")
def delete_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        project.delete()
        messages.success(request, "Project berhasil dihapus!")
        return redirect("main:show_projects")

    return redirect("main:show_projects")

def show_awards(request):
    json_response = get_awards_json(request)

    awards = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    awards = [award.object for award in awards]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Filza Shafira",
        "project_list": awards,
        "title_query": title_query,
    }
    return render(request, "award.html", context)

@login_required(login_url="/login/")
def create_award(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    
    form = AwardForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Penghargaan baru berhasil ditambahkan!")
        return redirect("main:show_awards")

    context = {
        "name": "Filza Shafira",
        "form": form,
    }
    return render(request, "awards_form.html", context)

def get_awards_json(request):
    title_query = request.GET.get("title", "").strip()
    awards = Award.objects.all()

    if title_query:
        awards = awards.filter(title__icontains=title_query)

    awards_json = serializers.serialize(
    "json", awards, use_natural_foreign_keys=True 
    )
    return HttpResponse(awards_json, content_type="application/json")

@login_required(login_url="/login/")
def delete_award(request, award_id):
    award = get_object_or_404(Award, pk=award_id)

    if request.method == "POST":
        award.delete()
        messages.success(request, "Penghargaan berhasil dihapus!")
        return redirect("main:show_awards")

    return redirect("main:show_awards")

def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Akun berhasil dibuat. Silakan login.")
        return redirect("main:login")

    context = {
        "name": "Filza Shafira",
        "form": form,
    }
    return render(request, "register.html", context)

def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        response = redirect("main:show_main")
        response.set_cookie('last_login', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return response

    context = {
        "name": "Filza Shafira",
        "form": form,
    }
    return render(request, "login.html", context)

def logout_user(request):
    logout(request)
    response = redirect("main:show_main")
    response.delete_cookie('last_login')
    return response

def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        response = redirect("main:show_main")
        response.set_cookie('last_login', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return response

    context = {
        "name": "Filza Shafira",
        "form": form,
    }
    return render(request, "login.html", context)

# Tanpa cek is_superuser: semua akun yang sudah login boleh memberi star
@login_required(login_url="/login/")
def toggle_star_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        # Kalau akun ini sudah pernah memberi star, batalkan star-nya.
        # Kalau belum, tambahkan star.
        if request.user in project.starred_by.all():
            project.starred_by.remove(request.user)
        else:
            project.starred_by.add(request.user)

    return redirect("main:show_projects")

# Tanpa cek is_superuser: semua akun yang sudah login boleh memberi star
@login_required(login_url="/login/")
def toggle_star_award(request, award_id):
    award = get_object_or_404(Award, pk=award_id)

    if request.method == "POST":
        # Kalau akun ini sudah pernah memberi star, batalkan star-nya.
        # Kalau belum, tambahkan star.
        if request.user in award.starred_by.all():
            award.starred_by.remove(request.user)
        else:
            award.starred_by.add(request.user)

    return redirect("main:show_awards")

