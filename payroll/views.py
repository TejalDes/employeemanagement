from django.shortcuts import render
from django.http import HttpResponse


def pay_details(request):
    print(request)
    return HttpResponse("Here are the pay details")
