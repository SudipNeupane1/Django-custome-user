from django.shortcuts import render
from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer


class PostList(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class=PostSerializer

    

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class=PostSerializer