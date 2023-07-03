from django.urls import path
from django.conf import settings
from . import views
from django.conf.urls.static import static
from .views import (PacienteListView, RegPaciente, PacienteDetailView, HistClinica, SearchResultsView, PacienteUpdateView, 
                    PacienteDeleteView, ReevaluacionesListView,
                    RegReevaluacion, ReevaluacionDetailView, ReevaluacionUpdateView, ReevaluacionDeleteView,
                    ReevaluacionesResultsView, ParaclinicosListView, RegParaclinico, ParaclinicoDetailView,
                    ParaclinicoUpdateView, ParaclinicosDeleteView, ParaclinicosSearchResultsView
                     )

app_name = "expediente"

expediente_patterns = ([
    #PACIENTES
    path('', PacienteListView.as_view(), name='pacientes'), 
    path('reg_paciente/', RegPaciente.as_view(), name='nuevo_paciente'),
    path('<int:pk>/<slug:paciente_slug>/', PacienteDetailView.as_view(), name='paciente'), #Resumen 
    path('update/<int:pk>/', PacienteUpdateView.as_view(),name='actualizar_paciente'),
    path('delete/<int:pk>/', PacienteDeleteView.as_view(),name='eliminar_paciente'),
    path("search/", SearchResultsView.as_view(), name="search_results"),

    path('historia_clinica/ <int:pk>', HistClinica.as_view(), name='historia_clinica'),

    #REEVALUACIONES
    path('reevaluaciones/', ReevaluacionesListView.as_view(), name='reevaluaciones'),
    path('reg_reevaluacion/', RegReevaluacion.as_view(), name='nueva_reevaluacion'),
    path('<int:pk>/', ReevaluacionDetailView.as_view(), name='reevaluacion'),
    path('update_reev/<int:pk>/', ReevaluacionUpdateView.as_view(),name='actualizar_reevaluacion'),
    path('delete_reev/<int:pk>/', ReevaluacionDeleteView.as_view(), name='eliminar_reevaluacion'),
    path("reevaluaciones_search/", ReevaluacionesResultsView.as_view(), name="reev_search_results"),

    #PARACLINICOS
    path('paraclinicos/', ParaclinicosListView.as_view(), name='paraclinicos'),
    path('reg_paraclinico/', RegParaclinico.as_view(), name='agregar_paraclinicos'),
    path('<int:pk>/<slug:paraclinico_slug>', ParaclinicoDetailView.as_view(), name='paraclinico'),
    path('update_paraclinico/<int:pk>/', ParaclinicoUpdateView.as_view(), name='actualizar_paraclinico'),
    path('delete_paraclinico/<int:pk>', ParaclinicosDeleteView.as_view(), name='eliminar_paraclinicos'),
    path('paraclinicos_search/', ParaclinicosSearchResultsView.as_view(), name='search_paraclinicos'),
    
   
   


], 'expediente')