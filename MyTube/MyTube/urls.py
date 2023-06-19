from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include(('app.urls', 'app'), namespace='app'))
]
urlpatterns += staticfiles_urlpatterns()
