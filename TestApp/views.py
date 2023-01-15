from django.urls import reverse_lazy
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib import messages
from TestApp.models import *
from TestApp.forms import *
# Create your views here.

class CandidateListView(ListView):
    model = Candidates
    template_name = "testapp/candidate/candidate_list.html"
    context_object_name = 'candidate'
    queryset = Candidates.objects.order_by('-created_at')


class CandidateCreateView(CreateView):
    model = Candidates
    template_name = 'testapp/candidate/candidate_form.html'
    form_class = Form_Candidate
    success_url = reverse_lazy('home_list')

    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, 'Creado con exito!')
        return super().form_valid(form)


class CandidateUpdateView(UpdateView):
    model = Candidates
    template_name = 'testapp/candidate/candidate_form.html'
    form_class = Form_Candidate
    success_url = reverse_lazy('home_list')

    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, 'Actualizado con exito!')
        return super().form_valid(form)


class CandidateDeleteView(DeleteView):
    model = Candidates
    template_name = 'testapp/candidate/candidate_delete.html'
    context_object_name = 'candidate'
    success_url = reverse_lazy('home_list')

    def post(self, request, *args, **kwargs):
        messages.add_message(self.request, messages.SUCCESS, 'Eliminado con exito!')
        return super().post(request, *args, **kwargs)


class TechnologyCandidateListView(ListView):
    model = TechnologyCandidate
    template_name = "testapp/tec_candidates/tec_candidate_list.html"
    context_object_name = 'tec_candidate'
    queryset = TechnologyCandidate.objects.order_by('-created_at')


class TechnologyCandidateCreateView(CreateView):
    model = TechnologyCandidate
    template_name = 'testapp/tec_candidates/tec_candidate_form.html'
    form_class = Form_TechnologyCandidate
    success_url = reverse_lazy('techno_candidate_list')

    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, 'Creado con exito!')
        return super().form_valid(form)


class TechnologyCandidateUpdateView(UpdateView):
    model = TechnologyCandidate
    template_name = 'testapp/tec_candidates/tec_candidate_form.html'
    form_class = Form_TechnologyCandidate
    success_url = reverse_lazy('techno_candidate_list')

    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, 'Actualizado con exito!')
        return super().form_valid(form)


class TechnologyCandidateDeleteView(DeleteView):
    model = TechnologyCandidate
    template_name = 'testapp/tec_candidates/tec_candidate_delete.html'
    context_object_name = 'tec_candidate'
    success_url = reverse_lazy('techno_candidate_list')

    def post(self, request, *args, **kwargs):
        messages.add_message(self.request, messages.SUCCESS, 'Eliminado con exito!')
        return super().post(request, *args, **kwargs)


def reporte(request, pk):
    tecnologia = get_object_or_404(Technology, pk=pk)
    # years = TechnologyCandidate.objects.filter(technology_id=tecnologia.id).all()
    # tipo_doc = models.Tipo_Documento.objects.filter(nivel=niveles.pk).all()
    # nivels = models.NivelEducativo.objects.exclude(id=niveles.id).all()
    return render(request, 'testapp/reporte.html',
                  {'tecnologia': tecnologia})