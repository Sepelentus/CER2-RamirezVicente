from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from core.models import Correspondencia
# Create your views here.

def home(request):
    correspondencia = Correspondencia.objects.all()
    context = {'correspondencia': correspondencia}
    return render(request, "core/body.html", context)
