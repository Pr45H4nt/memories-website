"""memoriesweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from memoriesapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',views.registerpage, name = "register" ),
    path('login/', views.loginpage, name = "loginpage"),
    path('logout/', views.logoutpage, name = "logout"),
    path('', views.home, name = "home"),
    path('add-memories/', views.Addmemory, name = "addmemory"),
    path('edit-memory/<slug>', views.edit_memory, name = "editmem"),
    path('delete-memory/<slug>', views.delete_item, name = "deletemem")
]
