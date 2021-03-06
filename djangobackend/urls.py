from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls')),
    path('', include('upload.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('authenticate.urls')),
]
