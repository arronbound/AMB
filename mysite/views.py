from django.views.generic import TemplateView
from django.views.generic import ListView
from polls.models import *

class ListPage(ListView):
    template_name = "aboutus.html"
    model = PersonWhoSignedUp

class AboutView(TemplateView):
    template_name = "index.html"
