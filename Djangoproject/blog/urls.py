from django.urls import path, include
from . import views
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static


router = routers.DefaultRouter()
router.register('post', views.PostViewSet)
router.register('comment', views.CommentViewSet)

urlpatterns = [
    path('<str:lang>/set_lang/', views.set_lang, name='set_lang'),
    path('', views.post_list, name='index'),
    # ex: /polls/5/
    path('<int:post_id>/', views.post_detail, name='detail'),
    path(
        '<int:post_id>/post_new_comment/',
        views.post_new_comment,
        name='postnewcomment'
        ),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('api/', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
