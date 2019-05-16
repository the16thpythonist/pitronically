from django.urls import path


from .views import project_detail_view, project_list_view


app_name = "blog"
urlpatterns = [
    # OWN URLS
    path("projects/", view=project_list_view, name="projects"),
    path("projects/<int:pk>/", view=project_detail_view, name="project_detail"),
]
