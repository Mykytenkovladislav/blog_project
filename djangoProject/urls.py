"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URL conf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import debug_toolbar
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

from blog_project.views import RegisterFormView, UpdateProfileView, UserDetailView, UsersListView
from djangoProject import settings

urlpatterns = [
                  path('', RedirectView.as_view(url='/blog/', permanent=True)),
                  path('blog/', include('blog_project.urls')),
                  path('accounts/', include('django.contrib.auth.urls')),
                  path('accounts/register/', RegisterFormView.as_view(), name='register'),
                  path('accounts/update_profile', UpdateProfileView.as_view(), name='update_profile'),
                  path('accounts/<int:pk>', UserDetailView.as_view(), name='user_detail'),
                  path('accounts/', UsersListView.as_view(), name='users_list'),
                  path('admin/', admin.site.urls),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
