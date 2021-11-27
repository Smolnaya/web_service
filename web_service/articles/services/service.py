from web_service.articles.models import Article


def articleToDictionary(article: Article):
    if article is None:
        return None

    dictionary = {"id": article.id, "title": article.title, "text": article.text,
                  "publication_date": article.publication_date, "topic": article.topic}

    return dictionary
