from django.urls import path

from main.views import show_main, show_experience, show_education, create_project, show_projects, delete_project, get_projects_json

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    path('education/', show_education, name='show_education'),
    path('project/', show_projects, name='show_projects'),
    path("project/add/", create_project, name="create_project"),
    path("api/projects/", get_projects_json, name="get_projects_json"),
    path("projects/<uuid:project_id>/delete/",delete_project,name="delete_project"),
]