"""
URL configuration for config project.

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
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('category/create', views.create_category, name='create_category'),
    path('category/edit', views.edit_category, name='edit_category'),
    path('category/<uuid:categoryId>/', views.delete_category, name='delete_category'),
    path('category/all', views.category_all, name='category_all'),
    path('calendar/all', views.calendar_all, name='calendar_all'),
    path('calendar/<uuid:calendarId>', views.calendar_detail, name='calendar_detail'),
    path('calendar/post', views.post_update, name='post_update'),
    path('calendar/post/finish', views.post_finish, name='post_finish'),
    path('calendar/post/create', views.post_create, name='post_create'),
    path('calendar/post/<uuid:postId>', views.post_delete, name='post_delete'),
    path('home/today', views.today_tasks, name='today_tasks'),
    path('home/all', views.all_tasks, name='all_tasks'),
    path('home/last_create', views.add_task, name='add_task'),
    path('home/last', views.last_tasks, name='last_tasks'),
    path('Setting/screen', views.screen_theme, name='screen_theme'),
    path('Setting/home', views.home_task, name='home_task'),
    path('theme/all/', views.theme_list, name='theme_list'),
    path('theme/<uuid:themeId>/', views.theme_detail, name='theme_detail'),
    path('theme/use/', views.theme_use, name='theme_use'),
]