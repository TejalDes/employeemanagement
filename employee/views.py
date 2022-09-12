from django.shortcuts import render
from django.http import HttpResponse


def emp_details(request):
    print(request.GET.get("message"))
    return HttpResponse("Here are the employee details")
