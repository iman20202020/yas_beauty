"""yas7 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include

from accounts.models import Teacher
from yas7 import settings



info_dict = {
    'queryset': Teacher.objects.all(),
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('teachme/', include('teachme.urls')),
    path('blog/', include('blog.urls')),
path('sitemap.xml', sitemap, # new
        {'sitemaps': {'accounts': GenericSitemap(info_dict, priority=0.6)}},
        name='django.contrib.sitemaps.views.sitemap'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "OSTADBAZ Admin"
admin.site.site_title = "OSTADBAZ Admin "
admin.site.index_title = "Welcome to OSTADBAZ "

