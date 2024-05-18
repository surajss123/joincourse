"""
URL configuration for project1 project.

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

from django.urls import path
from . import views
# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
   
    path('home2/', views.sign_Up, name="signup"),
    path('home3/', views.signUp, name="signup"),
    path('home1/', views.signIn, name="signin"),
    path('home4/', views.sura4, name="home"),
    path('home5/', views.navbar),
    path('home6/', views.about, name="about"),
    path('home7/', views.course, name="course"),
    path('home8/', views.condact, name="condact")

] 