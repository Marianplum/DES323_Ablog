# myapi/serializers.py
from rest_framework import serializers
from .models import Blog
from .models import dashb


class BlogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"


class DashbSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = dashb
        fields = "__all__"