from django.urls import path
from .views import post_list
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

]
