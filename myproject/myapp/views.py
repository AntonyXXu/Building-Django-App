from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
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

def register(req):
    if req.method == 'POST':
        username = req.POST['username']
        email = req.POST['email']
        password = req.POST['password']
        if User.objects.filter(email=email).exists():
            messages.info(req, 'email exists')
            return redirect('register')
        elif User.objects.filter(username=username).exists():
            messages.info(req, 'username exists')
            return redirect('register')
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            return redirect('login')
    return render(req,"register.html")
