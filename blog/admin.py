from django.contrib import admin

from blog.models import Blog

from django.contrib import admin

from seo.admin import ModelInstanceSeoInline

from blog.models import Blog

@admin.register(Blog)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ModelInstanceSeoInline]
