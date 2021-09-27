"""try_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, re_path, include #url
from werewolf.views import(
    
    were_wolf_create_veiw,
    
)





from .veiws import (
    home_page,
    contact_page,
    about_page,
    example_page,
  
)
urlpatterns = [
    re_path(r'^pages?/$',about_page),
    re_path(r'^about/$',about_page),
    path('',home_page),
     
    
    path('blog-new/' ,were_wolf_create_veiw),
    path('blog/', include('werewolf.urls')) ,
    

    path('about/',about_page),
    path('contact/',contact_page),
    path('admin/', admin.site.urls),
    path('example/',example_page),
]
