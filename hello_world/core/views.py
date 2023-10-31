from django.shortcuts import render

def index(request):
    context = {
        "title": "Ablog",
    }
    return render(request, "index.html", context)

def home(request):
    context = {"title": "Home"}
    return render(request, "home.html", context=context)
