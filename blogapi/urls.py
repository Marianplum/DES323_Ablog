from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'Blog', views.BlogViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('/tts',views.textToSpeech),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]