from django.shortcuts import render
from .models import BlogPost
from rest_framework.views import APIView, Response
from rest_framework.generics import ListAPIView
from rest_framework import status
from .serializers import BlogPostSerializer


class BlogList(ListAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
