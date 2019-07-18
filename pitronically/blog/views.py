

# Django standard library imports
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.http import HttpResponse
from django.views.generic import View, RedirectView
from django.shortcuts import render, get_object_or_404

# Third party imports

# Project wide imports
from .models import Project
from .mixins import NavbarMixin, SidebarMixin

User = get_user_model()




# ############
# VIEW CLASSES
# ############


class ProjectListView(SidebarMixin, NavbarMixin, View):

    def get(self, request):
        projects = Project.most_recent(20)
        context = {
            'title': 'Recent Projects',
            'projects': projects
        }
        context = self.context_navitems(context)
        context = self.context_sidebar(context)
        return render(request, 'blog/project_list.html', context)


project_list_view = ProjectListView.as_view()


class ProjectDetailView(SidebarMixin, NavbarMixin, View):

    def __init__(self, *args, **kwargs):
        super(ProjectDetailView, self).__init__(*args, **kwargs)

    def get(self, request, pk):
        project = get_object_or_404(Project, pk=pk)
        context = {
            'object': project
        }
        context = self.context_navitems(context)
        context = self.context_sidebar(context)
        return render(request, 'blog/project_detail.html', context)


project_detail_view = ProjectDetailView.as_view()


# ####################
# EDITOR RELATED VIEWS
# ####################


