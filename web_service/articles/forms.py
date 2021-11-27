from django import forms

from .models import Article


class ArticleForm(forms.ModelForm):
    title = forms.CharField(label='Заголовок')
    text = forms.CharField(label='Текст', widget=forms.Textarea)
    publication_date = forms.DateField(label='Дата публикации')
    topic = forms.CharField(label='Категория')

    class Meta:
        model = Article
        fields = ('title',
                  'text',
                  'publication_date',
                  'topic')
