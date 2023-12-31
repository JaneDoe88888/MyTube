from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include(('app.urls', 'app'), namespace='app')),
    path('users/', include(('users.urls', 'users'), namespace='users')),
    path('studio/', include(('studio.urls', 'studio'), namespace='studio')),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
