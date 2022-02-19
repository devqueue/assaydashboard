from django.urls import path, re_path
from dashboard import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    path('', views.indexpage, name='home'),
    path('samples', views.sample, name='sample'),
    path('revenue', views.revenue, name='revenue'),
    path('util', views.util, name='utilization'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)