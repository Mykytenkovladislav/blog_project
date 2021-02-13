from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.base import TemplateView

from django.shortcuts import render

from blog_project.forms import RegisterForm


class Index(TemplateView):
    template_name = 'index.html'


class RegisterFormView(generic.FormView):
    template_name = 'registration/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        form.save()

        username = self.request.POST['username']
        password = self.request.POST['password1']

        user = authenticate(username=username, password=password)
        login(self.request, user)
        return super(RegisterFormView, self).form_valid(form)
