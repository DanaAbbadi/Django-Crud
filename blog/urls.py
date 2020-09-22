from .views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView
from django.urls import path

urlpatterns = [ 
path ('', BlogListView.as_view() , name = 'blog'),
path('post/<int:pk>/', BlogDetailView.as_view(), name = 'details'),
path('post/new/', BlogCreateView.as_view(), name = 'new'),
path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name = 'update'),
path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name = 'delete'),
]