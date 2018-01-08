from django.urls import path
from .views import post_list, post_id, post_new_comment
from . import views


urlpatterns = [
    path('', post_list, name='index'),
    # ex: /polls/5/
    path('<int:post_id>/', views.post_id, name='detail'),
    path('<int:post_id>/post_new_comment/', views.post_new_comment, name='postnewcomment'),

]
