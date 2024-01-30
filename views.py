from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

from .models import SubjectMaster
# define homepage method

def homePage(request):

    srecs = SubjectMaster.objects.all()
    
    return HttpResponse("QUIZ APPLICATION TEST PAGE")
    
