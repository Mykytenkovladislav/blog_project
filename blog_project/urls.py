from django.urls import path

from blog_project.views import Index

urlpatterns = [
    path('', Index.as_view(), name='index'),
]
