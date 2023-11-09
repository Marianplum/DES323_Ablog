from django.shortcuts import render
import requests
import json
from datetime import datetime
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponseRedirect
import re
from rest_framework.response import Response
from django.http import HttpResponseNotFound

def index(request):
    context = {
        "title": "Ablog",
    }
    return render(request, "index.html", context)

@csrf_protect
def blog_post(request):

    if request.method == "POST":
        print('form data :', request.POST )
        ##pass text to tss api
        url = "http://127.0.0.1:8000/api/tts"
        payload = {'text':request.POST.get("content")}
        payload_json = json.dumps(payload)
        res = requests.post(url, data=payload_json, headers={'Content-Type': 'application/json'})

        if res.status_code == 200:
            print('API call was successful')
            api_response = res.json()  
            print('API response:', api_response)

            url2 = "http://127.0.0.1:8000/apiBlog/"
            payload2 = {
                            "title": request.POST.get("title"),
                            "picUrl": request.POST.get("picUrl"),
                            "content": request.POST.get("content"),
                            "audio_path": api_response['filepath'],
                            "file_size": api_response['filesize'],
                            "view": 1,
                        }
            payload2_json = json.dumps(payload2)
            res2 = requests.post(url2, data=payload2_json, headers={'Content-Type': 'application/json'})
            if res2.status_code == 201:
                print('API call was successful')
                api_response2 = res2.json()  
                print('API response:', api_response2)

                match = re.search(r'(\d+)(?!.*\d)', api_response2['url'])
                if match:
                    number = int(match.group())
                    redirect_url = f'/detail/{number}'
                    return HttpResponseRedirect(redirect_url)
                else:
                    return HttpResponseRedirect('/home')

                
            else:
                print('API 2 call failed with status code:', res2.status_code, res2.text)
                return HttpResponseRedirect('/blogpost')
        else:
            print('API call failed with status code:', res.status_code, res.text)


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

    if request.method == "POST" and request.POST.get('_method') == 'delete':
        delete_url = "http://127.0.0.1:8000/apiBlog/"+str(blogid)+"/"
        res = requests.delete(delete_url)
        if res.status_code == 204:
            print('API call was successful')
            data = {'message': 'Blog post deleted successfully', 'deleted': True}
            return render(request, "ablog/popup.html",data)
        
        else:
            print('API call failed with status code:', res.status_code, res.text)
            redirect = '/detail/'+str(blogid)
            return HttpResponseRedirect(redirect)
            


    ##call api to get blog detail
    url = "http://127.0.0.1:8000/apiBlog/"+str(blogid)+"/"

    res = requests.get(url)

    if res.status_code == 200:

        api_data = res.json()

        

        date_obj = datetime.strptime(api_data['date_create'], '%Y-%m-%dT%H:%M:%S.%fZ')
        formatted_date = date_obj.strftime('%d / %m / %Y')

        audio_path = api_data['audio_path']
        audio_path = audio_path[len('hello_world/static/'):] 

        dataObj = { 
            "coverImage" : api_data['picUrl'],
            "topic" : api_data['title'],
            "date" : formatted_date,
            "content" : api_data['content'],
            "file_path" : audio_path,
            "file_size" : api_data['file_size'],
            "url" : api_data['url'],
        }
        
        context = {
            "title" : "BlogDetail",
            "id": blogid,
            "data": dataObj,
        }
        return render(request, "ablog/detail.html", context=context)
    
    else:
        print('API call failed with status code:', res.status_code, res.text)
        return HttpResponseNotFound('<h1>404 NOT FOUND</h1>')


