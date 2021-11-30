from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string
from classification_service.classifier import predict_topic

from .models import Article
from .forms import ArticleForm
from .services.service import articleToDictionary


def article_list(request):
    return render(request, "articles/article_list.html")


def classification(request):
    return render(request, "articles/cf.html")


def predict_category(request):
    text_json = request.GET.get('data_text')
    topic = {'topic': predict_topic(text_json)}
    return JsonResponse(topic, safe=False)


def search_articles(request):
    search = request.GET.get('search')
    sort = request.GET.get('sort')
    topic = request.GET.get('topic')
    dateFrom = request.GET.get('dateFrom')
    dateTo = request.GET.get('dateTo')

    if search:
        lst = Article.objects.filter(title__icontains=search)
    else:
        lst = Article.objects.all()

    if topic:
        lst = lst.filter(topic__contains=topic)

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


def get_topics(request):
    lst = Article.objects \
        .values_list('topic', flat=True) \
        .order_by('topic') \
        .distinct()

    response = {
        'topics': list(lst)
    }

    return JsonResponse(response, safe=False)


def getArticles():
    article_list = Article.objects.all()
    sort = ''
    search = ''
    topic = ''
    dateFrom = ''
    dateTo = ''
    if sort:
        article_list = Article.objects.order_by(sort)
    if search:
        article_list = article_list.filter(Q(title__icontains=search))
    if topic:
        article_list.filter(Q(topic__icontains=topic))
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
