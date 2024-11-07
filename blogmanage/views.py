from django.shortcuts import render
from .models import BlogPost
from rest_framework.views import APIView, Response
from rest_framework.generics import (
    ListAPIView, RetrieveAPIView, CreateAPIView
)
from rest_framework import status
from .serializers import BlogPostSerializer


class BlogList(ListAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer


class BlogRetriveView(RetrieveAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    lookup_field = 'id'

class BlogCreateView(CreateAPIView):
    # queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    
    