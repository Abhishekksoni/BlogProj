from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
urlpatterns = [
    # path('', views.home , name='blog1-home'),
    path('about/', views.about , name='blog1-about'),


    path('', PostListView.as_view(), name = 'blog1-home'),

    path('post-new/', PostCreateView.as_view(), name = 'blog1-new'),

    path('post/<int:pk>/', PostDetailView.as_view(), name = 'blog1-detail'),

    

    path('post/<int:pk>/update/', PostUpdateView.as_view(), name = 'blog1-update'),

    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name = 'blog1-delete'),
]