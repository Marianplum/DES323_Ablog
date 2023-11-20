from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'Blog', views.BlogViewSet)
router.register(r'Dash', views.DashViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('/tts',views.textToSpeech),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('/test_dash', views.dash_data),
    path('/see_dash', views.see_dash_data),
]