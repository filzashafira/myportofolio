from django.urls import path

from main.views import show_main, show_experience,  show_education, create_project, show_projects, get_projects_json, delete_project, create_award, show_awards,  get_awards_json, delete_award, register, login_user, logout_user, toggle_star_project,toggle_star_award 

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    path('education/', show_education, name='show_education'),
    path("projects/add/", create_project, name="create_project"),
    path("projects/", show_projects, name="show_projects"),
    path("api/projects/", get_projects_json, name="get_projects_json"),
    path("projects/<uuid:project_id>/delete/",delete_project,name="delete_project"),
    path("awards/add/", create_award, name="create_award"),
    path("awards/", show_awards, name="show_awards"),
    path("api/awards/", get_awards_json, name="get_awards_json"),
    path("awards/<uuid:award_id>/delete/",delete_award,name="delete_award"),
    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    path(
        "projects/<uuid:project_id>/star/",
        toggle_star_project,
        name="toggle_star_project",
    ),
    path(
        "awards/<uuid:award_id>/star/",
        toggle_star_award,
        name="toggle_star_award",
    ),
]