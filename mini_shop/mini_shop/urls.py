from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from mini_shop import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('catalog.urls', namespace='catalog')),
    path('about/', include('about.urls', namespace='about')),
    path('auth/', include('users.urls')),
    path('auth/', include('django.contrib.auth.urls')),
    path('cart/', include('cart.urls', namespace='cart')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
