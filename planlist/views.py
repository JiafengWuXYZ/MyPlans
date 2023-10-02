from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def plan_list(request):
    return HttpResponse("这里是计划列表")
