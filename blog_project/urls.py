from django.urls import path

from blog_project import views

urlpatterns = [
    path('', views.PostList.as_view(), name='index'),
    path('<int:pk>', views.PostDetail.as_view(), name='post_detail'),
    path('post_create/', views.PostCreate.as_view(), name='post_create')
]
