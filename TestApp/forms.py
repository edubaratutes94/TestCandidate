from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from django.views.generic.edit import BaseUpdateView, DeleteView
from django import forms
from django.contrib import messages
from django.forms import widgets, TextInput, Textarea, EmailInput
from django.http import HttpResponseRedirect

from TestApp.models import *



# FORM candidate

class Form_Candidate(forms.ModelForm):
    class Meta:
        model = Candidates
        fields = [
            'name',
            'last_name',
            'address',
            'ci',
            'age',
            'sex',
        ]
        widgets = {
            "name": widgets.TextInput(attrs={'class': ' form-control', 'required': 'required'}),
            "last_name": widgets.TextInput(attrs={'class': ' form-control', 'required': 'required'}),
            "address": widgets.TextInput(attrs={'class': ' form-control', 'required': 'required'}),
            "sex": widgets.TextInput(attrs={'class': ' form-control', 'required': 'required'}),
            "ci": widgets.TextInput(attrs={'class': ' form-control', 'required': 'required'}),
            "age": widgets.NumberInput(attrs={'class': ' form-control', 'required': 'required'}),

            # "descripcion": widgets.Textarea(attrs={'class': ' form-control', 'required': 'required'}),
            # "email": widgets.EmailInput(attrs={'class': ' form-control'}),
            # "groups": widgets.SelectMultiple(attrs={'class': ' form-control'}),
            # "is_active": widgets.CheckboxInput(attrs={'class': ' form-control'}),
            # "imagen": widgets.FileInput(attrs={'class': ' form-control'}),
        }


# FORM technology candidate years

class Form_TechnologyCandidate(forms.ModelForm):
    class Meta:
        model = TechnologyCandidate
        fields = [
            'year',
            'candidate',
            'technology',

        ]
        widgets = {
            "year": widgets.NumberInput(attrs={'class': ' form-control', 'required': 'required'}),
            "candidate": widgets.Select(attrs={'class': ' form-control', 'required': 'required'}),
            "technology": widgets.Select(attrs={'class': ' form-control', 'required': 'required'}),

            # "descripcion": widgets.Textarea(attrs={'class': ' form-control', 'required': 'required'}),
            # "email": widgets.EmailInput(attrs={'class': ' form-control'}),
            # "groups": widgets.SelectMultiple(attrs={'class': ' form-control'}),
            # "is_active": widgets.CheckboxInput(attrs={'class': ' form-control'}),
            # "imagen": widgets.FileInput(attrs={'class': ' form-control'}),
        }

# class Update_Consejo(UpdateView):
#     model = models.ConsejoPopular
#     form_class = Form_Consejo
#     template_name = ('BodegaApp/consejo_form.html')
#     success_url = reverse_lazy('consejo_listar')
#
#     def post(self, request, *args, **kwargs):
#         register_logs(request, models.ConsejoPopular, self.get_object().pk, self.get_object().__str__(), 2)
#         # notify.send(request.user , recipient=self.get_object(), verb='Se han modificado sus datos', level='warning')
#         self.object = self.get_object()
#         messages.success(request, "Consejo modificado con éxito")
#         return super(BaseUpdateView, self).post(request, *args, **kwargs)
#
# class Delete_Consejo(DeleteView):
#     model = models.ConsejoPopular
#     success_url = reverse_lazy('consejo_listar')
#
#     def delete(self, request, *args, **kwargs):
#         register_logs(request, models.ConsejoPopular, self.get_object().pk, self.get_object().__str__(), 3)
#         self.object = self.get_object()
#         success_url = self.get_success_url()
#         self.object.delete()
#         messages.success(request, "Consejo eliminado con éxito")
#         return HttpResponseRedirect(success_url)


# ## TIPO DE PROCESO
#
# class Form_tipoProceso(forms.ModelForm):
#     class Meta:
#         model = models.tipo_proceso
#         fields = [
#             'nombre',
#
#         ]
#         widgets = {
#             "nombre": widgets.TextInput(attrs={'class': ' form-control', 'required': 'required'}),
#
#         }
#
# class Update_tipoProceso(UpdateView):
#     model = models.tipo_proceso
#     form_class = Form_tipoProceso
#     template_name = ('BodegaApp/tipo_proceso_form.html')
#     success_url = reverse_lazy('tipo_proceso_listar')
#
#     def post(self, request, *args, **kwargs):
#         register_logs(request, models.tipo_proceso, self.get_object().pk, self.get_object().__str__(), 2)
#         # notify.send(request,'Se han modificado sus datos', level='warning')
#         self.object = self.get_object()
#         messages.success(request, "Tipo de Proceso modificado con éxito")
#         return super(BaseUpdateView, self).post(request, *args, **kwargs)
#
# class Delete_tipoProceso(DeleteView):
#     model = models.tipo_proceso
#     success_url = reverse_lazy('tipo_proceso_listar')
#
#     def delete(self, request, *args, **kwargs):
#         register_logs(request, models.tipo_proceso, self.get_object().pk, self.get_object().__str__(), 3)
#         self.object = self.get_object()
#         success_url = self.get_success_url()
#         self.object.delete()
#         messages.success(request, "Tipo de Proceso eliminado con éxito")
#         return HttpResponseRedirect(success_url)
#
#
# # FORM PROCESO
#
# class Form_Proceso(forms.ModelForm):
#     class Meta:
#         model = models.Proceso
#         fields = [
#             'tipo_proceso',
#             'tipo_producto',
#             'descripcion',
#             'imagen',
#
#         ]
#         widgets = {
#             "tipo_proceso": widgets.Select(attrs={'class': ' form-control', 'required': 'required'}),
#             "tipo_producto": widgets.Select(attrs={'class': ' form-control', 'required': 'required'}),
#             "descripcion": widgets.Textarea(attrs={'class': ' form-control', 'required': 'required'}),
#             # "imagen": widgets.FileInput(attrs={'class': ' form-control'}),
#         }
#
# class Update_Proceso(UpdateView):
#     model = models.Proceso
#     form_class = Form_Proceso
#     template_name = ('BodegaApp/proceso_form.html')
#     success_url = reverse_lazy('proceso_listar')
#
#     def post(self, request, *args, **kwargs):
#         register_logs(request, models.Proceso, self.get_object().pk, self.get_object().__str__(), 2)
#         # notify.send(request.user , recipient=self.get_object(), verb='Se han modificado sus datos', level='warning')
#         self.object = self.get_object()
#         messages.success(request, "Proceso modificado con éxito")
#         return super(BaseUpdateView, self).post(request, *args, **kwargs)
#
# class Delete_Proceso(DeleteView):
#     model = models.Proceso
#     success_url = reverse_lazy('proceso_listar')
#
#     def delete(self, request, *args, **kwargs):
#         register_logs(request, models.Proceso, self.get_object().pk, self.get_object().__str__(), 3)
#         self.object = self.get_object()
#         success_url = self.get_success_url()
#         self.object.delete()
#         messages.success(request, "Proceso eliminado con éxito")
#         return HttpResponseRedirect(success_url)
#
# ## Contactos
#
# class Form_Contactos(forms.ModelForm):
#     class Meta:
#         model = models.Contacto
#         fields = [
#             'titulo',
#             'descripcion',
#             'imagen',
#
#         ]
#         widgets = {
#             "titulo": widgets.TextInput(attrs={'class': ' form-control', 'required': 'required'}),
#             "descripcion": widgets.Textarea(attrs={'class': ' form-control', 'required': 'required'}),
#             # "email": widgets.EmailInput(attrs={'class': ' form-control'}),
#             # "groups": widgets.SelectMultiple(attrs={'class': ' form-control'}),
#             # "is_active": widgets.CheckboxInput(attrs={'class': ' form-control'}),
#             # "imagen": widgets.FileInput(attrs={'class': ' form-control'}),
#         }
#
# class Update_Contactos(UpdateView):
#     model = models.Contacto
#     form_class = Form_Contactos
#     template_name = ('BodegaApp/contacto_form.html')
#     success_url = reverse_lazy('contacto_listar')
#
#     def post(self, request, *args, **kwargs):
#         register_logs(request, models.Contacto, self.get_object().pk, self.get_object().__str__(), 2)
#         # notify.send(request.user , recipient=self.get_object(), verb='Se han modificado sus datos', level='warning')
#         self.object = self.get_object()
#         messages.success(request, "Contacto modificado con éxito")
#         return super(BaseUpdateView, self).post(request, *args, **kwargs)
#
# class Delete_Contactos(DeleteView):
#     model = models.Contacto
#     success_url = reverse_lazy('contacto_listar')
#
#     def delete(self, request, *args, **kwargs):
#         register_logs(request, models.Contacto, self.get_object().pk, self.get_object().__str__(), 3)
#         self.object = self.get_object()
#         success_url = self.get_success_url()
#         self.object.delete()
#         messages.success(request, "Contacto eliminado con éxito")
#         return HttpResponseRedirect(success_url)
#
#
# ## QUIENES SOMOS
#
# class Form_Empresa(forms.ModelForm):
#     class Meta:
#         model = models.Empresa
#         fields = [
#             'nombre',
#             'resumen',
#             'descripcion',
#             'imagen',
#             'correo',
#             'correo_1',
#             'telefono',
#             'telefono_2',
#             'direccion',
#             'facebook',
#             'twitter',
#             'instagram',
#
#         ]
#         widgets = {
#             "nombre": widgets.TextInput(attrs={'class': ' form-control', 'required': 'required'}),
#             "resumen": widgets.Textarea(attrs={'class': ' form-control', 'required': 'required'}),
#             "descripcion": widgets.Textarea(attrs={'class': ' form-control', 'required': 'required'}),
#             "correo": widgets.EmailInput(attrs={'class': ' form-control'}),
#             "correo_1": widgets.EmailInput(attrs={'class': ' form-control'}),
#             "telefono": widgets.TextInput(attrs={'class': ' form-control' ,'required': 'required'}),
#             "telefono_2": widgets.TextInput(attrs={'class': ' form-control'}),
#             "direccion": widgets.TextInput(attrs={'class': ' form-control'}),
#             "facebook": widgets.TextInput(attrs={'class': ' form-control'}),
#             "twitter": widgets.TextInput(attrs={'class': ' form-control'}),
#             "instagram": widgets.TextInput(attrs={'class': ' form-control'}),
#         }
#
# class Update_Empresa(UpdateView):
#     model = models.Empresa
#     form_class = Form_Empresa
#     template_name = ('BodegaApp/empresa_form.html')
#     success_url = reverse_lazy('empresa_listar')
#
#     def post(self, request, *args, **kwargs):
#         register_logs(request, models.Empresa, self.get_object().pk, self.get_object().__str__(), 2)
#         # notify.send(request.user , recipient=self.get_object(), verb='Se han modificado sus datos', level='warning')
#         self.object = self.get_object()
#         messages.success(request, "Empresa modificada con éxito")
#         return super(BaseUpdateView, self).post(request, *args, **kwargs)
#
# class Delete_Empresa(DeleteView):
#     model = models.Empresa
#     success_url = reverse_lazy('empresa_listar')
#
#     def delete(self, request, *args, **kwargs):
#         register_logs(request, models.Empresa, self.get_object().pk, self.get_object().__str__(), 3)
#         self.object = self.get_object()
#         success_url = self.get_success_url()
#         self.object.delete()
#         messages.success(request, "Empresa eliminado con éxito")
#         return HttpResponseRedirect(success_url)
#
#
# class ComentarioForm(forms.Form):
#     nombre = forms.CharField(label="Nombre", required=True, widget=forms.TextInput(
#         attrs={'class': 'form-control', 'placeholder': 'Nombre', 'autocomplete': 'off'}))
#     correo = forms.EmailField(label="Email", required=True, widget=forms.EmailInput(
#         attrs={'class': 'form-control', 'placeholder': 'Email', 'autocomplete': 'off'}))
#     mensaje = forms.CharField(label="Mensaje", required=True, widget=forms.Textarea(
#         attrs={'class': 'form-control', 'placeholder': 'Mensaje', 'autocomplete': 'off'}))
#
# class Delete_Comentario(DeleteView):
#     model = models.Comentario
#     success_url = reverse_lazy('comentario_listar')
#
#     def delete(self, request, *args, **kwargs):
#         register_logs(request, models.Comentario, self.get_object().pk, self.get_object().__str__(), 3)
#         self.object = self.get_object()
#         success_url = self.get_success_url()
#         self.object.delete()
#         messages.success(request, "Comentario eliminado con éxito")
#         return HttpResponseRedirect(success_url)
#
#
