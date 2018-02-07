from django.shortcuts import render
from .models import Course

# Create your views here.


def courses(request):
    template_name = 'courses/courses.html'
    cursos = Course.objects.all()
    context = {
        'cursos':cursos
    }
    return render(request, template_name, context)

def details(request, pk):
    curso = Course.objects.get(pk=pk)
    context = {
        'curso':curso
    }
    template_name = 'courses/detail.html'
    return render(request, template_name, context)
