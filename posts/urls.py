from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns, static
from django.conf import settings
from .views import Create, Detail, Update, Delete

urlpatterns = [

    path('create', Create, name='create'),
    path('<str:slug>/', Detail, name='detail'),
    path('<str:slug>/update', Update, name='update'),
    path('<str:slug>/delete', Delete, name='delete'),
]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
