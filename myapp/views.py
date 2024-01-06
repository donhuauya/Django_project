# from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def testext(request):
    return HttpResponse("This is the local page")

def otherpage(request):
    return HttpResponse("OtherPage")