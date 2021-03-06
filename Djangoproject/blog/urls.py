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
    path('<int:post_id>/', views.post_detail, name='detail'),
    path(
        '<int:post_id>/post_new_comment/',
        views.post_new_comment,
        name='postnewcomment'
        ),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('api/', include(router.urls)),
    path(
        'account_activation_sent/',
        views.account_activation_sent,
        name='account_activation_sent'
        ),
    path(
         'account_activation_invalid/',
         views.account_activation_invalid,
         name='account_activation_invalid'
         ),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
