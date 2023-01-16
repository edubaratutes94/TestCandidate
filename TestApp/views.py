from django.urls import reverse_lazy
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib import messages
import sweetify
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
        sweetify.success(self.request, 'Creado correctamente!', button='Ok', timer=5000)
        return super().form_valid(form)


class CandidateUpdateView(UpdateView):
    model = Candidates
    template_name = 'testapp/candidate/candidate_form.html'
    form_class = Form_Candidate
    success_url = reverse_lazy('home_list')

    def form_valid(self, form):
        sweetify.success(self.request, 'Actualizado con exito!', button='Ok', timer=5000)
        return super().form_valid(form)


class CandidateDeleteView(DeleteView):
    model = Candidates
    template_name = 'testapp/candidate/candidate_delete.html'
    context_object_name = 'candidate'
    success_url = reverse_lazy('home_list')

    def post(self, request, *args, **kwargs):
        sweetify.success(self.request, 'Eliminado con exito!', button='Ok', timer=5000)
        return super().post(request, *args, **kwargs)


class TechnologyCandidateListView(ListView):
    model = TechnologyCandidate
    template_name = "testapp/tec_candidates/tec_candidate_list.html"
    context_object_name = 'tec_candidate'
    queryset = TechnologyCandidate.objects.order_by('-created_at')


def technology_candidate_create(request):
    tecno = TechnologyCandidate.objects.all()
    if request.POST:
        form = Form_TechnologyCandidate(request.POST)
        if form.is_valid():
            year = form.cleaned_data['year']
            technology = form.cleaned_data['technology']
            candidate = form.cleaned_data['candidate']
            if tecno.filter(technology=technology, candidate=candidate).exists():
                sweetify.error(request, 'Error, ya existe esta persona con esa tecnologia!', button='Ok', timer=5000)
            else:
                elemento = tecno.create(year=year, technology=technology,
                                        candidate=candidate,
                                        )
                sweetify.success(request, 'Creado correctamente!', button='Ok', timer=5000)
            return HttpResponseRedirect('/technology_candidate')
        else:
            sweetify.error(request, 'Error, en el formulario!', button='Ok', timer=5000)
    else:
        form = Form_TechnologyCandidate()
    args = {}
    args['form'] = form
    return render(request, 'testapp/tec_candidates/tec_candidate_form.html', args)

class TechnologyCandidateUpdateView(UpdateView):
    model = TechnologyCandidate
    template_name = 'testapp/tec_candidates/tec_candidate_form.html'
    form_class = Form_TechnologyCandidate
    success_url = reverse_lazy('techno_candidate_list')

    def form_valid(self, form):
        sweetify.success(self.request, 'Actualizado con exito!', button='Ok', timer=5000)
        return super().form_valid(form)


class TechnologyCandidateDeleteView(DeleteView):
    model = TechnologyCandidate
    template_name = 'testapp/tec_candidates/tec_candidate_delete.html'
    context_object_name = 'tec_candidate'
    success_url = reverse_lazy('techno_candidate_list')

    def post(self, request, *args, **kwargs):
        sweetify.success(request, 'Eliminado con exito!', button='Ok', timer=5000)
        return super().post(request, *args, **kwargs)


def reporte(request, pk):
    tecnologia = get_object_or_404(Technology, pk=pk)
    return render(request, 'testapp/reporte.html',
                  {'tecnologia': tecnologia})
