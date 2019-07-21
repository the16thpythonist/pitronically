from django.urls import path
from django.views.generic import RedirectView
from django.urls import reverse_lazy

from .views import project_detail_view, project_list_view

# 20.07.2019
# Added the path "", which is when only "/blog" is being typed in. In this case a redirect to the actual projects
# list view will happen.
app_name = "blog"
urlpatterns = [
    # OWN URLS
    path("", view=RedirectView.as_view(url=reverse_lazy('blog:projects'))),
    path("projects/", view=project_list_view, name="projects"),
    path("projects/<int:pk>/", view=project_detail_view, name="project_detail"),
]
