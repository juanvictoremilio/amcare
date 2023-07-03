from django.http import Http404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from .models import Paciente, Reevaluacion, Paraclinicos
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import PacienteForm, ReevaluacionForm, ParaclinicosForm

# Create your views here.

#REGISTRO DE PACIENTES

class SearchResultsView(LoginRequiredMixin, ListView):
    model = Paciente
    template_name = 'search_results.html'

    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        object_list = Paciente.objects.filter(
            Q(name__icontains=query) | Q(phone__icontains=query)
        )
        return object_list

class PacienteListView(LoginRequiredMixin, ListView):
    model = Paciente
    template_name = 'paciente_list.html'
    context_object_name = 'paciente_list'

    def get_queryset(self):
        return Paciente.objects.filter(user=self.request.user)
    

class RegPaciente(LoginRequiredMixin, CreateView):
    model = Paciente
    form_class = PacienteForm
    success_url = reverse_lazy('expediente:pacientes')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

#def user_paciente_create(request):
#    user_data = PacienteForm.get_user_data(request.user)
#    return render(request, 'paciente_form.html', {'user_data': user_data})

class PacienteDetailView(LoginRequiredMixin, DetailView):
    model = Paciente
    template_name = 'paciente_detail.html'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        if obj.user != self.request.user:
            raise Http404("No tienes permiso para ver este resumen.")
        return obj
    
class HistClinica(LoginRequiredMixin, DetailView):
    model = Paciente
    template_name = 'historia_clinica.html'

class PacienteUpdateView(LoginRequiredMixin, UpdateView):
    model = Paciente
    form_class = PacienteForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('expediente:actualizar_paciente', args=[self.object.id]) + '?ok'

class PacienteDeleteView(LoginRequiredMixin, DeleteView):
    model = Paciente
    success_url = reverse_lazy('expediente:pacientes')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        if obj.user != self.request.user:
            raise Http404("No tienes permiso para eliminar este objeto.")
        return obj

#REEVALUACIONES

class ReevaluacionesResultsView(LoginRequiredMixin, ListView):
    model = Reevaluacion
    template_name = 'searchreev_results.html'

    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        object_list = Reevaluacion.objects.filter(
            Q(paciente__icontains=query)
        )
        return object_list
    

class ReevaluacionesListView(LoginRequiredMixin, ListView):
    model = Reevaluacion
    template_name = 'reevaluaciones_list.html'

    def get_queryset(self):
        return Reevaluacion.objects.filter(user=self.request.user)

class RegReevaluacion(LoginRequiredMixin, CreateView):
    model = Reevaluacion
    form_class = ReevaluacionForm
    success_url = reverse_lazy('expediente:reevaluaciones')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ReevaluacionDetailView(LoginRequiredMixin, DetailView):
    model = Reevaluacion
    template_name = 'reevaluacion_detail.html'

class ReevaluacionUpdateView(LoginRequiredMixin, UpdateView):
    model = Reevaluacion
    form_class = ReevaluacionForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('expediente:actualizar_reevaluacion', args=[self.object.id]) + '?ok'

class ReevaluacionDeleteView(LoginRequiredMixin, DeleteView):
    model = Reevaluacion
    success_url = reverse_lazy('expediente:reevaluaciones')

#PARACLINICOS

class ParaclinicosSearchResultsView(LoginRequiredMixin, ListView):
    model = Paraclinicos
    template_name = 'searchparaclinicos_results.html'

    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        object_list = Paraclinicos.objects.filter(
            Q(pac__icontains=query)
        )
        return object_list

class ParaclinicosListView(LoginRequiredMixin, ListView):
    model = Paraclinicos
    template_name = 'paraclinicos_list.html'

class RegParaclinico(LoginRequiredMixin, CreateView):
    model = Paraclinicos
    form_class = ParaclinicosForm
    success_url = reverse_lazy('expediente:paraclinicos')

class ParaclinicoDetailView(LoginRequiredMixin, DetailView):
    model = Paraclinicos
    template_name = 'paraclinico_detail.html'

class ParaclinicoUpdateView(LoginRequiredMixin, UpdateView):
    model = Paraclinicos
    form_class = ParaclinicosForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('expediente:actualizar_paraclinico', args=[self.object.id]) + '?ok'

class ParaclinicosDeleteView(LoginRequiredMixin, DeleteView):
    model = Paraclinicos
    success_url = reverse_lazy('expediente:paraclinicos')
