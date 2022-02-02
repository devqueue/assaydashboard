
from django.urls import re_path
from dashboard import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    re_path(r'^utilization$',views.utilizationApi),
    re_path(r'^utilization/([0-9]+)$',views.utilizationApi),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)