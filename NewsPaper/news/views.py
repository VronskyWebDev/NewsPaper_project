# from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from django.views.generic import DetailView


class PostList(ListView):
    model = Post  # указываем модель, объекты которой мы будем выводить
    template_name = 'news.html'
    context_object_name = 'news'


class PostDetail(DetailView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'news'
