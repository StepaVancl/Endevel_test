from django.contrib import admin

from .models import Article, ArticleTag, Tag


admin.site.register(Article)
admin.site.register(ArticleTag)
admin.site.register(Tag)
