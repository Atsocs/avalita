from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    url(r'^accounts/', include('allauth.urls')),
    path('avalita/', include('avalita.urls')),
    path('admin/', admin.site.urls),
]
