 # coding=utf-8

import json
import re
from django.contrib import messages
from django.contrib.admin.models import LogEntry, DELETION
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.contenttypes.models import ContentType
from django.contrib.messages.views import SuccessMessageMixin
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.encoding import force_str
from django.views.generic import View

def validate_carne(value):
    """
    @Desc: Funcion para validar entrada de solo 11 dígitos en el carné de identidad del empleado.
    """
    p = re.compile(u"\d+$")
    a = re.compile(u"([0-9]{2})(0?[1-9]|1[012])(0?[1-9]|[12][0-9]|3[01])([0-9]{5})$")
    m = p.match(value)
    l = a.match(value)

    # validar mes con dias
    mes = str(value[2:4])
    dia = str(value[4:6])
    error_dia = ""
    error_mes = ""


    if mes == "01" or mes == "03" or mes == "05" or mes == "07" or mes == "08" or mes == "10" or mes == "12":
        if int(dia) > 31 or int(dia) < 1:
            error_dia = "Tiene error en el dia del carne"
    else:
        if mes == '02':
            if int(dia)>29 or int(dia)<1:
                error_dia = "Recuerde que febrero tiene solo 28-29 días, arregle el carne"
        else:
            if int(dia)>31 or int(dia)<1:
                error_dia = "Error en el dia en el carne"
    if not m:
        raise ValidationError(u'Solo se admiten números.')
    if not l:
        raise ValidationError(u'Esta incorrecta la estructura del carnet de identidad.')
    if value.__len__() != 11:
        raise ValidationError(u'El carné de identidad debe contener 11 dígitos.')
    if error_dia != "":
        raise ValidationError(error_dia)
    if error_mes != "":
        raise ValidationError(error_mes)


def validate_only_numbers(value):
    """
    @Desc: Funcion para validar entrada de solo números
    """
    array = str(value).split(".")
    p = re.compile(u"[0-9]+$")
    if array.__len__()>1:
        m = p.match(array[0])
        n = p.match(array[1])
        if not m or not n:
            raise ValidationError(u'Solo se admiten números.')
    elif array.__len__()==1:
        m = p.match(array[0])
        if not m:
            raise ValidationError(u'Solo se admiten números.')

