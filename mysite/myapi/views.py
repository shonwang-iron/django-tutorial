from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.http.response import JsonResponse
# Create your views here.
from rest_framework import viewsets
from rest_framework.decorators import api_view

from .models import Employee

def home(request):
    return HttpResponse('Welcome Home')

@api_view(['GET'])
def employee_all(request):
    employees = Employee.objects.all()
    return render(request, 'employee_all.html', {'employees': employees})

@api_view(['GET'])
def employee_detail(request, employee_id):
    try:
        employee = Employee.objects.get(id=employee_id)
    except Employee.DoesNotExist:
        raise Http404('Employee Not Found')
    return render(request, 'employee_detail.html', {'employee': employee})