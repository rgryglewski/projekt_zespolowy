from django.shortcuts import render, redirect
from django.views.generic import TemplateView


# Create your views here.


class Index(TemplateView):
    template_name = "index.html"


class About(TemplateView):
    template_name = "about.html"


def account(request):
    return redirect('/accounts/login')
