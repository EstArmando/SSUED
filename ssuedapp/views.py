from django.db.models import Count, Case, When, IntegerField, Value
import json
from django.shortcuts import render

from student.models import Student

# Create your views here.


def index(request):
    """ bar = (
          Student.objects
          .values('university__name')
          .annotate(total_discapacitados=Count('disability'))
      )

    pie = (
        Student.objects
        .values('sex__gender')
        .annotate(count=Count('sex__gender'))
    )

    # Calcula el total de estudiantes
    total_estudiantes = sum(d['count'] for d in pie)

    # Calcula el porcentaje de cada sexo
    for d in pie:
      d['porcentaje'] = round((d['count'] / total_estudiantes) * 100, 2)

    pie2 = (
        Student.objects
        .values('disability__type')
        .annotate(count=Count('disability__type'))
    )

    # Calcula el total de estudiantes
    total_estudiantes = sum(d['count'] for d in pie2)

    # Calcula el porcentaje de cada discapacidad
    for d in pie2:
      d['porcentaje'] = round((d['count'] / total_estudiantes) * 100, 2)

    bar_json = json.dumps(list(bar))
    pie_json = json.dumps(list(pie))
    pie2_json = json.dumps(list(pie2)) """

    return render(request, 'index.html', {
        'title': 'Inicio',
        # 'bar': bar_json,
        # 'pie': pie_json,
        # 'pie2': pie2_json,
    })
