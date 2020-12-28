from django.contrib import admin
from django.urls import path,include
 

urlpatterns = [
    path('', include('pages.urls')),
    path('admin/', admin.site.urls),
    path('users/',include('users.urls')), #Urls for Signup Page
    path('users/',include('django.contrib.auth.urls')), #urls for Login and Signup page ,prepared by Django itsef

]
