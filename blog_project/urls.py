from django.urls import path

from blog_project import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='index'),
    path('<int:pk>', views.PostDetailView.as_view(), name='post_detail'),
    path('post_create/', views.PostCreateView.as_view(), name='post_create'),

]
