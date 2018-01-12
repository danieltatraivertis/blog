from django.urls import path, include
from .views import post_list, register
from . import views

urlpatterns = [
    path('', post_list, name='index'),
    # ex: /polls/5/
    path('<int:post_id>/', views.post_detail, name='detail'),
    path(
        '<int:post_id>/post_new_comment/',
        views.post_new_comment,
        name='postnewcomment'
        ),
    path('accounts/', include('django.contrib.auth.urls'), name='login'),
    path('accounts/', include('django.contrib.auth.urls'), name='logout'),
    path('accounts/', include('django.contrib.auth.urls'), name='profile'),
    path('register/', register, name='register'),

]