from django.shortcuts import render
from django.views.generic.base import TemplateView 
from django.views.generic.detail import DetailView

# Create your views here.

class HomePageView(TemplateView):
    template_name = "core/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Tittle'] = 'EASKVLAPIVS'
        return context
    
class WellcomePageView(TemplateView):
    template_name = "core/wellcome.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Tittle'] = 'EASKVLAPIVS'
        return context

class SamplePageView(TemplateView):
    template_name = "core/sample.html"


