from django import http
from django.http import HttpResponse
from django.template import Template, Context
from datetime import date, datetime


def primer_vista(request):
    return HttpResponse('Primera pagina 23/03/2022 <3')

def segunda_vista(request):
    return HttpResponse('<h1>Titulo 1</h1> <p>Esto es un parrafo </p>')

def dia_hora(request):
    fecha_hora = datetime.now()
    return HttpResponse(f'<p>Tiempo actual: {fecha_hora}</p>')

def nombre_usuario (request, nombre):
    return HttpResponse (f'Tu nombre es {nombre.capitalize()}')

def calculo (request, edad):
    anioNac = 2022 - int(edad)
    return HttpResponse (f'Su año de naciemiento es: {anioNac}')

def pagina_inicio (request):
    archivo = open(r'C:\Users\Bruno Donato\Documents\DJANGO1\proyecto_coder\proyecto_coder\templates\page.html','r')
    
    plantilla = Template(archivo.read())

    archivo.close()

    context = Context()

    documento = plantilla.render(context)
     
    return HttpResponse(documento)