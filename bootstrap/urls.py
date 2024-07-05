"""
URL configuration for bootstrap project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from app.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("bs_comp/",bs_comp,name='bs_comp'),
    path("bs_alerts/",bs_alerts,name='bs_alerts'),
    path("bs_badges/",bs_badges,name='bs_badges'),
    path("bs_breadcrumb/",bs_breadcrumb,name='bs_breadcrumb'),
    path("bs_buttons/",bs_buttons,name='bs_buttons'),
    path("bs_cards/",bs_cards,name='bs_cards'),
    path("bs_carousel/",bs_carousel,name='bs_carousel'),
    path("bs_forms/",bs_forms,name='bs_forms'),
    path("bs_carousel_download/",bs_carousel_download,name='bs_carousel_download'),
    path("bs_inputgrp/",bs_inputgrp,name='bs_inputgrp'),
    
]
