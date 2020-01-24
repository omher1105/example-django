from datetime import date, datetime

from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render

from persona.models import PersonaModel


class PersonaForm(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=100)
    apellido = forms.CharField(label='Apellido', max_length=100)
    direccion = forms.CharField(label='Direccion', max_length=100, required=False)


def helloWorldView(request):
    context = {
        'saludo': 'Hola Mundo'
    }
    return render(request, 'hola-mundo.html', context=context)


def personaView(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            persona = dict()
            data = request.POST
            persona['nombre'] = data['nombre']
            persona['apellido'] = data['apellido']
            persona['direccion'] = data['direccion']
            persona['edad'] = 26
            persona['fecha_nacimiento'] = datetime(2020, 5, 1)
            PersonaModel.objects.create(**persona)
            return HttpResponseRedirect('/thanks')
    else:
        form = PersonaForm()
    return render(request, 'persona-form.html', {'form': form})


def thanksView(request):
    persona = PersonaModel.objects.get(pk=1)
    persona.apellido = 'hernandez'
    persona.save()
    context = {
        'nombre': persona.nombre
    }
    return render(request, 'thanks.html', context=context)
