from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy, reverse

# Create your views here.

class BlogListView(ListView):
    template_name = 'blog.html'
    model = Post

class BlogDetailView(DetailView):
    template_name = 'details.html'
    model = Post

class BlogCreateView(CreateView):
    template_name = 'new.html'
    model = Post
    fields = ['title', 'author', 'body']

class BlogUpdateView(UpdateView):
    template_name = 'update.html'
    model = Post
    fields = ['title', 'author', 'body']   

class BlogDeleteView(DeleteView):
    template_name = 'delete.html'
    model = Post
    success_url = reverse_lazy('blog')