from datetime import datetime, timedelta
from django.shortcuts import render, redirect, get_object_or_404
from .models import Writer, Article
from .forms import ArticleForm
from .constants import ArticleStatus
from django.db.models import Count
from django.db.models import OuterRef, Subquery


def article_approval(request):
    article = Article.objects.filter(status=ArticleStatus.PENDING.value)
    context = {'article': article}
    return render(request, 'approve_articles.html', context)


def articles_edited(request):
    article = Article.objects.filter(edited_by=request.user.writer)
    context = {'article': article}
    return render(request, 'edited_articles.html', context)


def dashboard(request):
    last_30_days = Article.objects.filter(created_at__lte=datetime.now(
    ), created_at__gt=datetime.now()-timedelta(days=30)).filter(written_by=OuterRef('pk')).values('written_by')
    last_30_days = last_30_days.annotate(
        dcount=Count('written_by')).values('dcount')

    data = Writer.objects.annotate(
        articles_count=Count('articles')).annotate(last_30_days=Subquery(last_30_days))
    context = {'article_count': data}
    return render(request, 'dashboard.html', context)


def all_articles(request):
    articles = Article.objects.order_by('-created_at')
    context = {'articles': articles}
    return render(request, 'all_articles.html', context)


def article_submit(request):
    form = ArticleForm()
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            instance = form.save()
            instance.written_by = request.user.writer or False
            instance.save()
            return redirect(f'/article/{instance.id}')
    context = {"form": form}

    return render(request, "article_form.html", context)


def articles_view(request, id):
    instance = get_object_or_404(Article, id=id)
    form = ArticleForm(request.POST or None,
                       instance=instance)
    if form.is_valid():
        form.save()
        return redirect('/articles/')
    return render(request, 'article_form.html', {'form': form})


def approved_article(request, id):
    instance = get_object_or_404(Article, id=id)
    instance.status = ArticleStatus.APPROVED.value
    instance.edited_by = request.user.writer
    instance.save()
    return redirect('approval')


def rejected_article(request, id):
    instance = get_object_or_404(Article, id=id)
    instance.status = ArticleStatus.REJECTED.value
    instance.edited_by = request.user.writer
    instance.save()
    return redirect('approval')
