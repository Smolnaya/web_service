import json
from django.http import HttpResponse

from django.core import serializers
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Article
from .forms import ArticleForm
from .services.service import articleToDictionary


def article_list(request):
    article_list = Article.objects.all()

    paginator = Paginator(article_list, 6)
    page = request.GET.get('page', 1)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        'articles': posts
    }
    return render(request, "articles/article_list.html", context)


def search_articles(request):
    search = request.GET.get('search')
    sort = request.GET.get('sort')
    author = request.GET.get('author')
    source = request.GET.get('source')
    dateFrom = request.GET.get('dateFrom')
    dateTo = request.GET.get('dateTo')


    if search:
        lst = Article.objects.filter(title__icontains=search)
    else:
        lst = Article.objects.all()

    if author:
        lst = lst.filter(author__contains=author)

    if source:
        lst = lst.filter(source__contains=source)

    if dateFrom:
        lst = lst.filter(publication_date__gte=dateFrom)

    if dateTo:
        lst = lst.filter(publication_date__lte=dateTo)

    lst = lst.order_by(sort)

    data = list()
    for article in lst:
        # article фильтр по заголовку
        data.append(articleToDictionary(article))


    return JsonResponse(data, safe=False)


def get_authors(request):
    lst = Article.objects \
        .values_list('author', flat=True) \
        .order_by('author') \
        .distinct()

    response = {
        'authors': list(lst)
    }

    return JsonResponse(response, safe=False)


def get_source(request):
    lst = Article.objects \
        .values_list('source', flat=True) \
        .order_by('source') \
        .distinct()

    response = {
        'sources': list(lst)
    }

    return JsonResponse(response, safe=False)


def getArticles():
    article_list = Article.objects.all()
    sort = ''
    search = ''
    author = ''
    source = ''
    dateFrom = ''
    dateTo = ''
    if sort:
        article_list = Article.objects.order_by(sort)
    if search:
        article_list = article_list.filter(Q(title__icontains=search))
    if author:
        article_list.filter(Q(author__icontains=author))
    if source:
        article_list.filter(Q(source__icontains=source))
    return article_list


def save_article_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            articles = Article.objects.all()
            data['html_article_list'] = render_to_string(
                'articles/includes/partial_article_list.html',
                {'articles': articles})
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def article_create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
    else:
        form = ArticleForm()
    return save_article_form(request, form, 'articles/includes/partial_article_create.html')


def article_open(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
    else:
        form = ArticleForm(instance=article)
    return save_article_form(request, form, 'articles/includes/partial_article_open.html')


def article_update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
    else:
        form = ArticleForm(instance=article)
    return save_article_form(request, form, 'articles/includes/partial_article_update.html')


def article_delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    data = dict()
    if request.method == 'POST':
        article.delete()
        data['form_is_valid'] = True
        articles = Article.objects.all()
        data['html_article_list'] = render_to_string('articles/includes/partial_article_list.html',
                                                     {
                                                         'articles': articles
                                                     })
    else:
        context = {'article': article}
        data['html_form'] = render_to_string('articles/includes/partial_article_delete.html',
                                             context, request=request)
    return JsonResponse(data)
