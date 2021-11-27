import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web_service.settings")
django.setup()

from web_service.articles.models import Article
import json


def insert_rows():
    for f in os.listdir('/Users/stacey_smolnaya/PycharmProjects/lentaru_crawler/files/json'):
        if not f.endswith('DS_Store'):
            with open(f'/Users/stacey_smolnaya/PycharmProjects/lentaru_crawler/files/json/{f}', 'r') as js:
                try:
                    l = js.read()
                    values = dict(json.loads(l))
                    article = Article()
                    article.publication_date = values['date']
                    article.title = values['title']
                    article.topic = values['topic']
                    article.text = values['text']
                    article.save()
                except Exception as e:
                    print(f'{e} - {f}')
                    pass


def delete_everything():
    Article.objects.all().delete()


if __name__ == "__main__":
    # delete_everything()
    insert_rows()
