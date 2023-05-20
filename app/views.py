from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def naru(request):
    return HttpResponse('<marquee><h1>mahesh is loving one girl that girl name is vanitha</h1></marquee>')

def neeru(request):
    return HttpResponse('<marquee><h1> if you have any problem strust the shiva and ram</h1></marquee>')

def poorna(request):
    return HttpResponse('<h1>mom and dad are the real gods for his chidrens</h1>')

def keerthi(request):
    return HttpResponse('<marquee><h1>narasimha is loving someone his name is keerthi</h1></marquee>')