from django.shortcuts import render
from app1 import binary1
from django.http import HttpResponse
# Create your views here.


def index(request,n1,n2):
    output = binary1.fun(n1,n2)
    return HttpResponse("<h1> The dictionary is %s</h1>" % output)
