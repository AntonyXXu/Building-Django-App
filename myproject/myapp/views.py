from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    name = "abc"
    return render(request, "index.html", {"name": name})

def counter(request):
    words = request.GET['text']
    length = len(words.split())
    context = {
        length: length
    }
    return render(request, "counter.html", context)