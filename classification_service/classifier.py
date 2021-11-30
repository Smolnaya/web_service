import pickle
import re
import pandas as pd
import pymorphy2
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.linear_model import SGDClassifier, LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from nltk.stem import SnowballStemmer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


def delete_symbols(data: str):
    data = re.sub(r"[^а-яА-я]+", " ", data)
    return data.lower()


def lemmatize(data: str):
    words = data.split(' ')
    filtered_words = []
    morph = pymorphy2.MorphAnalyzer()
    for word in words:
        if word:
            w = morph.parse(word)[0]
            filtered_words.append(w.normal_form)
    return filtered_words


def delete_stopwords(data: list, stop_words: list):
    return [word for word in data if word not in stop_words]


def stemming(data: list):
    snowball = SnowballStemmer(language='russian')
    stemmed = set()
    for s in data:
        stemmed.add(snowball.stem(s))
    return list(stemmed)


def load_stops():
    stops = []
    with open('files/stop-ru.txt') as file:
        for word in file.readlines():
            stops.append(word.strip().lower())
    return stops


def clean_text(data: str):
    stopwords = load_stops()
    data = delete_symbols(data)  # удалить лишние символы, к нижнему регистру
    data = lemmatize(data)  # к начальной форме
    data = delete_stopwords(data, stopwords)  # удаление стоп-слов
    data = stemming(data)  # до корня
    data = ' '.join(data)
    return data


def predict_topic(text: str):
    text = [clean_text(text)]
    with open('../documentation/lr.pkl', 'rb') as training_model:
        model = pickle.load(training_model)

    prediction = model.predict(text)
    return prediction[0]


def model_training():
    # Очистка данных
    # csv_file = pd.read_csv('files/dataset.csv', encoding='UTF-8', sep='#%')
    # for i in tqdm(range(len(csv_file))):
    #     with open('files/cleaned_dataset.csv', 'a', encoding='UTF-8') as file:
    #         file.write(f'{csv_file["topic"][i]}#%{clean_text(csv_file["text"][i])}\n')

    # Загрузка данных
    csv_file = pd.read_csv('files/cleaned_dataset.csv', encoding='UTF-8', sep='#%')

    # Разделение данных для обучения и тестирования
    x = csv_file['text']
    y = csv_file['topic']
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=100)

    # Обучение классификатора MultinomialNB
    nb = Pipeline([
        ('vect', CountVectorizer()),
        ('tfidf', TfidfTransformer()),
        ('clf', MultinomialNB())
    ])
    nb.fit(x_train, y_train)
    y_pred_nb = nb.predict(x_test)
    print(f'NB accuracy: {accuracy_score(y_pred_nb, y_test)}')

    # Обучение классификатора SGDClassifier
    sgd = Pipeline([
        ('vect', CountVectorizer()),
        ('tfidf', TfidfTransformer()),
        ('clf', SGDClassifier(loss='hinge', penalty='l2', alpha=1e-3, random_state=32, max_iter=5, tol=None))
    ])
    sgd.fit(x_train, y_train)
    y_pred_sgd = sgd.predict(x_test)
    print(f'SGD accuracy: {accuracy_score(y_pred_sgd, y_test)}')

    # Обучение классификатора LogisticRegression
    lr = Pipeline([
        ('vect', CountVectorizer()),
        ('tfidf', TfidfTransformer()),
        ('clf', LogisticRegression(C=1.5, random_state=100))
    ])
    lr.fit(x_train, y_train)
    y_pred_lr = lr.predict(x_test)
    print(f'LR accuracy: {accuracy_score(y_pred_lr, y_test)}')

    # NB accuracy: 0.8005
    # SGD accuracy: 0.8315
    # LR accuracy: 0.864

    # Сохранение классификатора в файл
    with open('../documentation/lr.pkl', 'wb') as file:
        pickle.dump(lr, file)
    print('Классификатор LR сохранен')

