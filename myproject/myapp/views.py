from django.shortcuts import render
from django.http import HttpResponse
from .models import Features
# Create your views here.
def index(request):
    name = "abc"
    f = Features()
    f.id = 0
    f.name = 'test'
    f.details = "abcdefghijklmnop"

    f1 = Features()
    f1.id = 0
    f1.name = 'test'
    f1.details = "abcdefghijklmnop"

    features = [f1, f2]
    return render(request, "index.html", {'features': features})

def counter(request):
    words = request.GET['text']
    length = len(words.split())
    context = {
        length: length
    }
    return render(request, "counter.html", context)

