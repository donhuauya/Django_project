# from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import project,tasks
from django.shortcuts import get_object_or_404

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


def projects(request):
    _project = list(project.objects.values())
    return JsonResponse(_project, safe=False)

def task(request,title):
    # task = tasks.objects.get(id=id)
    # tas = get_object_or_404(tasks, id=id)
    tas = tasks.objects.get(title=title)
    return HttpResponse("task: %s" % tas.title)

