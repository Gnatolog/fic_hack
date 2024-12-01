from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse
import datetime
from templateapp.templates.dogovor_uslugi.request import AIRequest as vozmezdieAI
from templateapp.templates.dogovor_ab.request import AIRequest as dogovorAI
from .task import start_help_filling
import sys
import json
sys.path.append("..")


class Dashboard(View):
    def get(self, request):
        return render(request,'templateapp/dashboard.html')


class DogovorVozmezdie(CreateView):
    def get(self, request):
        return render(request,'dogovor_uslugi/fill.html')
    def post(self, request):
        zakaz = request.POST.get('zakaz')
        ispolnitel = request.POST.get('ispolnitel')
        result = vozmezdieAI(zakaz, ispolnitel)
        return render(request, 'dogovor_uslugi/edit.html', context={"result": result,
                                                                       'result_str': json.dumps(result,
                                                                                                ensure_ascii=False)})

class DogovorAB(CreateView):
    def get(self, request):
        return render(request,'dogovor_ab/fill.html')
    def post(self, request):
        zakaz = request.POST.get('zakaz')
        result = dogovorAI(zakaz)
        return render(request, 'dogovor_ab/edit.html', context={"result": result})


def test_celery(request):
    result = start_help_filling()
    return render(request, 'templateapp/dashboard.html')



def work_provision_fill(request):
    return render(request,'templateapp/fill.html')

def work_provision_edit(request):
    return render(request,'templateapp/edit.html')


def change_action(request):
    return render(request,'templateapp/midle_page.html')




