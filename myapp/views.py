# from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("index page")

def testext(request, username):
    print(username)
    result = username + ", welcome"
    return HttpResponse("<h2>Hello %s</h2>" % result)

def testnum(request, id):
    print(type(id))
    result = id +100 /3
    return HttpResponse("<h2>Hello %s</h2>" % result)

def otherpage(request):
    return HttpResponse("OtherPage")