from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=32)
    article_text = models.TextField()
    picture_url = models.URLField(max_length=256, blank=True)


class Tag(models.Model):
    tag = models.CharField(max_length=32)


class ArticleTag(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
