import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web_service.settings")
django.setup()

from web_service.articles.models import Article
from lxml import etree
from os import listdir
from os.path import join as joinpath
import datetime


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
        article.href = root.find('href').text
        article.source = root.find('source').text
        tags = root.find('tags')
        article.tags = ', '.join(map(lambda elem: elem.text, tags))

        article.save()


# files = 'D:\\Asus\\Documents\\files'
# loadFiles(files)
