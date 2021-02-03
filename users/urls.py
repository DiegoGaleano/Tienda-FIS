"""Market URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# Users urls
from users import views as users_views

# Base view api
from users import viewsApi

#API REST
from rest_framework import routers
router = routers.DefaultRouter()

#API
# En el router vamos añadiendo los endpoints a los viewsets
router.register('list', viewsApi.ProfileViewSet)


urlpatterns = [
    # path('ej1/', posts_views.list_posts_ej1, name="post_ej"),
    path('api/', include(router.urls)),
]
