"""socialDex URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts', views.posts),
    path('', views.registerpage, name='registerpage'),
    path('login', views.loginpage, name='loginpage'),
    path('post_list', views.post_list, name='post_list'),
    path('users_posts', views.users_posts, name='users_posts'),
    path('post_detail/<int:pk>', views.post_detail, name='post_detail'),
    path('user/<int:id>', views.user_id, name='user_id'),
    path('new_post', views.new_post, name='new_post'),
    path('login_error', views.login_error, name='login_error'),
    path('logout', views.logoutpage, name='logoutpage'),
    path('last_posts', views.last_posts, name='last_posts'),
    path('search_results', views.search_results, name='search_results'),
]
