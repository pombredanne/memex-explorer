"""Base views."""

from django.shortcuts import render
from django.views import generic
from django.views.generic import ListView, TemplateView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.exceptions import ValidationError
from django.utils.text import slugify

from base.models import Project
from base.forms import AddProjectForm, ProjectSettingsForm


def project_context_processor(request):
    return {
        'projects': Project.objects.all(),
    }


class IndexView(ListView):
    model = Project
    template_name = "base/index.html"


class AboutView(TemplateView):
    template_name = "base/about.html"
    

class AddProjectView(SuccessMessageMixin, CreateView):
    model = Project
    form_class = AddProjectForm
    template_name = "base/add_project.html"
    success_message = "Project %(name)s was added successfully."

    def get_success_url(self):
        return self.object.get_absolute_url()


class ProjectView(DetailView):
    model = Project
    slug_url_kwarg = 'project_slug'
    template_name = "base/project.html"


class ProjectSettingsView(SuccessMessageMixin, UpdateView):
    model = Project
    slug_url_kwarg = 'project_slug'
    form_class = ProjectSettingsForm
    success_message = "Project %(name)s was edited successfully."
    template_name_suffix = '_update_form'

