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
    2. Add a URL to urlpatterns:  path('yasblog/', include('yasblog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include

from accounts.sitemaps import TeacherSitemap
from forum.sitemaps import PostSitemap
from yas7 import settings

sitemaps = {
    'teachers': TeacherSitemap,
    'posts': PostSitemap,
}


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('course/', include('teachme.urls')),
    # path('blog/', include('blog.urls')),
    path('blog/', include('forum.urls')),
    path('ratings/', include('star_ratings.urls', namespace='ratings')),



    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "OSTADBAZ Admin"
admin.site.site_title = "OSTADBAZ Admin "
admin.site.index_title = "Welcome to OSTADBAZ "

