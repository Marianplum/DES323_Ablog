from django.shortcuts import render

def index(request):
    context = {
        "title": "Ablog",
    }
    return render(request, "ablog/index.html", context)

def blog_post(request):
    context = {}
    return render(request, "ablog/blog-post.html", context=context)