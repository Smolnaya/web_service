from django import forms

from .models import Article


class ArticleForm(forms.ModelForm):
    title = forms.CharField(label='Заголовок')
    author = forms.CharField(label='Автор')
    text = forms.CharField(label='Текст', widget=forms.Textarea)
    publication_date = forms.DateField(label='Дата публикации')
    source = forms.CharField(label='Источник')
    tags = forms.CharField(label='Тег')

    class Meta:
        model = Article
        fields = ('title',
                  'author',
                  'text',
                  'publication_date',
                  'source',
                  'tags')
