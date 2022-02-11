
from django.urls import path, re_path
from dashboard import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    # re_path(r'^utilization$',views.utilizationApi),
    # re_path(r'^utilization/([0-9]+)$',views.utilizationApi),
    # re_path(r'^processapi$', views.processedApi),
    # re_path(r'^processapi/([0-9]+)$', views.processedApi),
    # re_path(r'^revenueapi$', views.revenueapi),
    # re_path(r'^revenueapi/([0-9]+)$', views.revenueapi),
    # re_path('^process$', views.processpage),
    # re_path('^revenue$', views.revenuepage),
    path('', views.indexpage, name='home'),
    path('samples', views.sample, name='sample'),
    path('revenue', views.revenue, name='revenue'),
    path('util', views.util, name='utilization'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)