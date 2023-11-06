# myapi/serializers.py
from rest_framework import serializers
from .models import Blog
class BlogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"