# Django standard library imports
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render, get_object_or_404
from django.template import loader


from .models import Project

# ###########
# VIEW MIXINS
# ###########


class NavbarMixin:

    NAVITEMS = {
        'Projects':     reverse_lazy('blog:projects')
    }

    def context_navitems(self, context: dict):
        navitems = self.NAVITEMS
        context.update({
            'navitems': navitems
        })
        return context


class SidebarMixin:

    RECENT_PROJECTS_COUNT = 10
    RECENT_PROJECTS_TITLE = "Most Recent Projects"

    def context_sidebar(self, context: dict):
        context.update({
            'sidebar': {
                'active':   True,
                'items':    [
                    self.most_recent_projects(),
                ]
            }
        })
        return context

    def most_recent_projects(self):
        projects = Project.most_recent(self.RECENT_PROJECTS_COUNT)
        context = {
            'title': self.RECENT_PROJECTS_TITLE,
            'projects': projects
        }
        html = loader.render_to_string('blog/sidebar_recent_projects.html', context)
        return html
