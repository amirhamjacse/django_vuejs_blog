from rest_framework import serializers
from .models import BlogPost, BlogCategory

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = [
            'id',
            'title',
            'blog_description',
            'is_active',
            'date',
        ]


class BlogCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = [
            'id',
            'name',
        ]
