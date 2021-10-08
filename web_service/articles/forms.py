from django import forms

from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title',
                  'author',
                  'text',
                  'publication_date',
                  'source',
                  'tags')