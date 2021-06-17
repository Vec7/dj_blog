from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render

# Create your views here.
def index(req):
    return HttpResponse('Good Return')


def categories(req, catid):
    raise Http404()
    #return HttpResponse(f'Good Return Categories : {catid}')


def pageNotFound(req, exeption):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')