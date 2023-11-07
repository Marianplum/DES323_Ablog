from django.shortcuts import render
import requests
import json
from datetime import datetime

def index(request):
    context = {
        "title": "Ablog",
    }
    return render(request, "index.html", context)

def blog_post(request):
    context = {}
    return render(request, "ablog/blog-post.html", context=context)

def home(request):
    url = "http://127.0.0.1:8000/apiBlog/"
    res = requests.get(url)
    api_data = res.json()
    
    context = {
        "title": "Home",
        "data" : api_data,
        }
    return render(request, "ablog/home.html", context=context)

def profile(request):
    context = {}
    return render(request, "ablog/profile.html", context=context)

def dashboard(request):
    url = "http://127.0.0.1:8000/apiBlog/"
    res = requests.get(url)
    api_data = res.json()

    context = {
        
    }
    return render(request, "ablog/dashboard.html", context=context)

def blogDetail(request,blogid):
    ##call api to get blog detail
    url = "http://127.0.0.1:8000/apiBlog/"+str(blogid)+"/"

    res = requests.get(url)

    api_data = res.json()

    date_obj = datetime.strptime(api_data['date_create'], '%Y-%m-%dT%H:%M:%S.%fZ')
    formatted_date = date_obj.strftime('%d / %m / %Y')

    dataObj = { 
        "coverImage" : "https://t3.ftcdn.net/jpg/05/91/97/64/360_F_591976463_KMZyV6obpsrN2bJJJkYW0bzoH2XxLTlA.jpg",
        "topic" : api_data['title'],
        "date" : formatted_date,
        "content" : api_data['content'],
        "file_path" : api_data['audio_path'],
        "file_size" : api_data['file_size'],
    }

    context = {
        "title" : "BlogDetail",
        "id": blogid,
        "data": dataObj
    }
    return render(request, "ablog/detail.html", context=context)

