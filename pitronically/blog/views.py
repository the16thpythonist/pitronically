# standard library
from itertools import chain
from operator import attrgetter

# Django standard library imports
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.http import HttpResponse
from django.utils import timezone
from django.views.generic import View, RedirectView
from django.shortcuts import render, get_object_or_404

# Third party imports

# Project wide imports
from .models import Project, Tutorial, Entry
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


class TutorialListView(SidebarMixin, NavbarMixin, View):

    def get(self, request):
        tutorials = Tutorial.most_recent(20)
        context = {
            'title':        'Recent Tutorials',
            'tutorials':    tutorials,
        }
        context = self.context_navitems(context)
        context = self.context_sidebar(context)
        return render(request, 'blog/tutorial_list.html', context)


tutorial_list_view = TutorialListView.as_view()


class TutorialDetailView(SidebarMixin, NavbarMixin, View):

    def get(self, request, pk):
        tutorial = get_object_or_404(Tutorial, pk=pk)
        context = {
            'object':   tutorial
        }
        context = self.context_sidebar(context)
        context = self.context_navitems(context)
        return render(request, 'blog/tutorial_detail.html', context)


tutorial_detail_view = TutorialDetailView.as_view()


class EntryListView(SidebarMixin, NavbarMixin, View):

    def get(self, request):
        projects = Project.objects.exclude(publishing_date__gte=timezone.now()).all()
        tutorials = Tutorial.objects.exclude(publishing_date__gte=timezone.now()).all()
        entries = sorted(
            chain(projects, tutorials),
            key=attrgetter('publishing_date'),
            reverse=True
        )[0:20]
        context = {
            'title':        'Recent Posts',
            'entries':      entries,
        }
        context = self.context_navitems(context)
        context = self.context_sidebar(context)
        return render(request, 'blog/entry_list.html', context)


entry_detail_view = EntryListView.as_view()


# ####################
# EDITOR RELATED VIEWS
# ####################


