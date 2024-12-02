from django.shortcuts import render
from .models import BlogPost, BlogCategory
from rest_framework.views import APIView, Response
from rest_framework.generics import (
    ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView,
    DestroyAPIView
)
from rest_framework.exceptions import NotFound
from rest_framework import status
from .serializers import (
    BlogPostSerializer,
    BlogCategorySerializer
)


class BlogList(ListAPIView):
    queryset = BlogPost.objects.all().order_by('-pk')
    serializer_class = BlogPostSerializer


class BlogRetriveView(RetrieveAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    lookup_field = 'id'


class BlogCreateView(CreateAPIView):
    serializer_class = BlogPostSerializer
    
    def get_queryset(self):
        # Optional: use this if you want to fetch categories in the response
        return BlogCategory.objects.all()
    
    def perform_create(self, serializer):
        # Get the category_id from the URL
        category_id = self.kwargs.get('category_id')
        try:
            # Retrieve the category instance
            category = BlogCategory.objects.get(id=category_id)
        except BlogPost.DoesNotExist:
            # Raise an error if the category does not exist
            print('not working')
            raise NotFound("Category not found")

        # Save the blog post with the retrieved category
        serializer.save(category=category)


class BlogUpdateView(UpdateAPIView):
    serializer_class = BlogPostSerializer
    queryset = BlogPost.objects.all()
    lookup_field = 'id'


class DestroyView(DestroyAPIView):
    serializer_class = BlogPostSerializer
    queryset = BlogPost.objects.all()
    lookup_field = 'id'


class CategoryList(ListAPIView):
    queryset = BlogCategory.objects.all().order_by('-pk')
    serializer_class = BlogCategorySerializer
