from django.shortcuts import render

def index(request):
    context = {
        "title": "Ablog",
    }
    return render(request, "index.html", context)

def blog_post(request):
    context = {}
    return render(request, "ablog/blog-post.html", context=context)
def home(request):
    context = {"title": "Home"}
    return render(request, "ablog/home.html", context=context)

def profile(request):
    context = {}
    return render(request, "ablog/profile.html", context=context)