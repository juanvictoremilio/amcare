from django.urls import path
from . import views
from core.views import HomePageView, SamplePageView, WellcomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),   
    path('sample/', SamplePageView.as_view(), name='sample'),
    path('wellcome/', WellcomePageView.as_view(), name='bienvenida'),
    


        ]