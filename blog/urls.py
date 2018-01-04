from django.urls import path
from .views import post_list
from .views import post_id
from . import views


urlpatterns = [
    path('', post_list),
    # ex: /polls/5/
    path('<int:post_id>/', views.post_id, name='detail'),

]
