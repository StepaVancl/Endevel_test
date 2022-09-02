from django.views.generic import TemplateView
from django.http import Http404

from .models import Article, Tag, ArticleTag
from .forms import BlogForm


class ArticlesView(TemplateView):
    template_name = "blog/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        blog_form = BlogForm(self.request.GET)
        blog_form.is_valid()
        cleaned_data = blog_form.cleaned_data
        tag_id = cleaned_data.get("tag_id", None)
        if tag_id is not None:
            try:
                tag = Tag.objects.get(pk=tag_id)
                article_tags = ArticleTag.objects.filter(tag=tag)
                article_ids = []
                for at in article_tags:
                    article_ids.append(at.article.id)

                # I assume automatic id -> greater id = newer article
                articles = Article.objects.filter(id__in=article_ids).order_by("id").reverse()
                context["articles"] = articles
                tags = Tag.objects.all()
                context["tags"] = tags
            except (Tag.DoesNotExist, ArticleTag.DoesNotExist, Article.DoesNotExist):
                raise Http404("Articles or tags or article_tag don't exist.")
            return context

        try:
            # I assume automatic id -> greater id = newer article
            articles = Article.objects.order_by("id").reverse()[:3]
            context["articles"] = articles
            tags = Tag.objects.all()
            context["tags"] = tags
        except (Article.DoesNotExist, Tag.DoesNotExist):
            raise Http404("Articles or tags don't exist.")
        return context


class ArticleDetailView(TemplateView):
    template_name = "blog/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            article = Article.objects.get(pk=self.kwargs.get("article_id"))
            article_tags = ArticleTag.objects.filter(article=article)
            tag_ids = []
            for at in article_tags:
                tag_ids.append(at.tag.id)
            tags = Tag.objects.filter(id__in=tag_ids)
            context["article"] = article
            context["tags"] = tags
        except Article.DoesNotExist:
            raise Http404("Articles or tags don't exist.")
        return context

