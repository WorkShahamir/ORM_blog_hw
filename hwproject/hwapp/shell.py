from django.utils import timezone
from .models import Author, Article, Publication

# Создаем авторов
Author.objects.create(name='Нурсултан Бердиев', email='nursultanberdiev@gmail.com', username='nursultanberdiev', date_register='2021-01-04')
Author.objects.create(name='Лю Вероника', email='ronilyu@gmail.com', username='ronik', date_register='2023-03-12')
Author.objects.create(name='Токтосунова Чынара', email='chynara0409@gmail.com', username='chynara', date_register='2023-11-21')

# Создаем статьи
nursultan = Author.objects.get(username='nursultanberdiev')
veronika = Author.objects.get(username='ronik')
chynara = Author.objects.get(username='chynara')

Article.objects.create(title='Что нужно для разработки мобильных приложений: языки и тренды', author=nursultan)
Article.objects.create(title='Зачем нужно использовать кроссплатформенную систему', author=nursultan)
Article.objects.create(title='Сравниваем Java и Python или с чего лучше начать', author=nursultan)
Article.objects.create(title='Новый ChatGPT-4: в чем его особенность', author=veronika)
Article.objects.create(title='История компании Boston Dynamics. Как появлялись их роботы', author=chynara)

# Опубликуем статьи
Publication.objects.bulk_create([
    Publication(author=nursultan, article=Article.objects.get(title='Что нужно для разработки мобильных приложений: языки и тренды'), date_published=timezone.now()),
    Publication(author=nursultan, article=Article.objects.get(title='Зачем нужно использовать кроссплатформенную систему'), date_published=timezone.now()),
    Publication(author=nursultan, article=Article.objects.get(title='Сравниваем Java и Python или с чего лучше начать'), date_published=timezone.now()),
    Publication(author=veronika, article=Article.objects.get(title='Новый ChatGPT-4: в чем его особенность'), date_published=timezone.now()),
    Publication(author=chynara, article=Article.objects.get(title='История компании Boston Dynamics. Как появлялись их роботы'), date_published=timezone.now()),
])

# Выводим всех авторов по дате регистрации
print('Авторы по дате регистрации:')
for author in Author.objects.order_by('date_register'):
    print(f'{author.name} ({author.username}) - {author.date_register}')

# Выводим статьи автора Nursultan
print('\nСтатьи автора Nursultan:')
for article in Article.objects.filter(author=nursultan):
    print(article.title)



