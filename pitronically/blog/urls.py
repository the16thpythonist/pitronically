from django.urls import path
from django.views.generic import RedirectView
from django.urls import reverse_lazy

from .views import project_detail_view, project_list_view, bet_list_view
from .views import tutorial_detail_view, tutorial_list_view, bet_detail_view
from .views import entry_detail_view

# 20.07.2019
# Added the path "", which is when only "/blog" is being typed in. In this case a redirect to the actual projects
# list view will happen.
# 25.08.2019
# Added the path to the tutorial pages
app_name = "blog"
urlpatterns = [
    # OWN URLS
    path("", view=entry_detail_view, name="entries"),
    path("projects/", view=project_list_view, name="projects"),
    path("projects/<int:pk>/", view=project_detail_view, name="project_detail"),
    path("tutorials/", view=tutorial_list_view, name="tutorials"),
    path("tutorials/<int:pk>/", view=tutorial_detail_view, name="tutorial_detail"),
    path("bets/", view=bet_list_view, name="bets"),
    path("bets/<int:pk>", view=bet_detail_view, name="bet_detail"),
]
