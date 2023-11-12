from django.shortcuts import render
import os
from google.oauth2 import service_account
from google.cloud import texttospeech
from django.http import HttpResponse
import json
import uuid
import time
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect


# Create your views here.
# views.py
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import BlogSerializer, DashbSerializer
from .models import Blog, dashb

import pandas as pd

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all().order_by('blog_id')
    serializer_class = BlogSerializer

class DashViewSet(viewsets.ModelViewSet):
    queryset = dashb.objects.all().order_by('dash_d_id')
    serializer_class = DashbSerializer


def dash_data(requset):
    url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQOb_cBK7r0kJ1f7ceZqJAFLBPz2Bka4lpqg8eplqZ2NGWtSZvEt4P35g0XtCB4cvbHw6J2sRv9cPOe/pub?gid=0&single=true&output=csv"
    df = pd.read_csv(url)
    df.dropna()
    data_sets = df[["num_views", "date", "ts"]]
    sucess = []
    errors = []
    for index, row in data_sets.iterrows():
        instance = dashb(
            view_d = int(row['num_views']),
            date_d = 'none'
        )

        try:
            instance.save()
            sucess.append(index)
        except:
            errors.append(index)

    return JsonResponse({"sucess_indexs":sucess, "error_indexs":errors})



@api_view(['POST'])
def textToSpeech(request):
    if request.method == 'POST':
        try:
            # Parse JSON data from the request body
            data = json.loads(request.body)
            text = data.get('text', "Hello, World!")  # Use the provided text or a default value {"text" : 'fggdfkgjsdflkgjsdklfgjsldfkgj'}

            # Generate a unique file name based on the current timestamp and a random ID
            extension = 'mp3'
            unique_filename = generate_unique_filename("output", extension)
            audio_file_path = os.path.join("hello_world/static/audiofile", unique_filename)

            client_file = os.environ['GOOGLE_APPLICATION_CREDENTIALS']
            credentials = service_account.Credentials.from_service_account_file(client_file)
            client = texttospeech.TextToSpeechClient(credentials=credentials)
            
            synthesis_input = texttospeech.SynthesisInput(text=text)

            voice = texttospeech.VoiceSelectionParams(
                language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
            )

            audio_config = texttospeech.AudioConfig(
                audio_encoding=texttospeech.AudioEncoding.MP3
            )

            response = client.synthesize_speech(
                input=synthesis_input, voice=voice, audio_config=audio_config
            )

            # Save the audio content with the unique file name
            with open(audio_file_path, "wb") as out:
                out.write(response.audio_content)
            
            file_size = os.path.getsize(audio_file_path)

            return JsonResponse({'filepath': audio_file_path,'filesize': file_size}, status=200)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON input'}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)

def generate_unique_filename(filename, extension):
    timestamp = int(time.time())  # Get the current timestamp
    unique_id = uuid.uuid4().hex  # Generate a random UUID

    # Combine the timestamp and random ID to create a unique file name
    unique_filename = f"{timestamp}_{unique_id}.{extension}"
    return unique_filename



# install latest version of Django Rest-framework
# pip install djangorestframework markdown django-filter django-cors-headers

# save package version requirements
# pip freeze > requirements.txt

# set environment for api google-cloud - texttospeech
# pip install --upgrade google-cloud-texttospeech