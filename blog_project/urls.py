from django.urls import path

from blog_project.views import PostListView, PostDetailView, PostCreateView, UserPostsListView, UpdatePostView

urlpatterns = [
    path('', PostListView.as_view(), name='index'),
    path('<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('post_create/', PostCreateView.as_view(), name='post_create'),
    path('my_posts', UserPostsListView.as_view(), name='user_posts'),
    path('my_posts/<int:pk>', UpdatePostView.as_view(), name='post_update'),

]
