from django.conf import settings
from django.conf.urls.static import static, staticfiles_urlpatterns
from django.contrib import admin
from django.urls import path, include
from .views import Home as home, fourZeroFour
from posts.views import Search
from users.views import signup, login, logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('signup', signup, name='signup'),
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
    path('results', Search, name='search'),
    path('ERROR', fourZeroFour, name='ERROR'),
    path('post/', include('posts.urls'))
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
