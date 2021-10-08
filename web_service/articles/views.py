from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Article
from .forms import ArticleForm


def article_list(request):
    article_list = Article.objects.all()
    query = request.GET.get('q')
    sort_by = request.GET.get('s')

    if query:
        article_list = Article.objects.filter(Q(title__icontains=query))

    if sort_by:
        article_list = article_list.order_by(sort_by)

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
