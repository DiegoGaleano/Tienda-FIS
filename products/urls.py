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

# Products urls
from products import views as productsviews

# Base view api
from products import viewsApi

#API REST
from rest_framework import routers
router = routers.DefaultRouter()

#API
# En el router vamos añadiendo los endpoints a los viewsets
router.register('list', viewsApi.ProductViewSet)
router.register('categories', viewsApi.CategoryViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
]