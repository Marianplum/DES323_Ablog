from django.shortcuts import render

def index(request):
    context = {
        "title": "Ablog",
    }
    return render(request, "ablog/index.html", context)

