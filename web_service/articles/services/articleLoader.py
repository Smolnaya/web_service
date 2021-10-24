import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web_service.settings")
django.setup()

from web_service.articles.models import Article
from lxml import etree
from os import listdir
from os.path import join as joinpath
import datetime


def cleanNulls():
    articleList = Article.objects.all()
    for article in articleList:
        if article.source == '':
            print('null value - ', article.title)
            article.source = None
            article.save()


def loadFiles(file):
    for path in listdir(file):
        article = Article()
        xmlFile = joinpath(file, path)

        with open(xmlFile, encoding='utf-8') as fobj:
            xml = fobj.read()

        root = etree.fromstring(xml)

        article.title = root.find('title').text
        article.author = root.find('author').text
        date = root.find('date').text
        dateT = datetime.date.fromisoformat('-'.join([date[:4], date[5:7], date[8:]]))
        article.publication_date = dateT
        article.text = root.find('text').text[10:-4]
        if not root.find('source').text:
            article.source = ''
        else:
            article.source = root.find('source').text

        tags = root.find('tags')
        for t in tags:
            if t is not None:
                article.tags = ''
            else:
                article.tags = ', '.join(map(lambda elem: elem.text, tags))
                break

        article.save()


if __name__ == "__main__":
    # cleanNulls()
    files = '/Users/stacey_smolnaya/PycharmProjects/collectionOfArticles/files'
    loadFiles(files)
