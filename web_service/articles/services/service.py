from web_service.articles.models import Article


def articleToDictionary(article: Article):
    if article == None:
        return None

    dictionary = {"id": article.id, "title": article.title, "author": article.author, "text": article.text,
                  "publication_date": article.publication_date, "source": article.source, "tags": article.tags}

    return dictionary
