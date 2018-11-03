from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from . import views


urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('<int:pk>/', PostDetailView.as_view(), name='blog-detail'),
    path('new/', PostCreateView.as_view(), name='blog-create'),
    path('<int:pk>/update/', PostUpdateView.as_view(), name='blog-update'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='blog-delete'),
    path('about/', views.about, name='blog-about'),
]