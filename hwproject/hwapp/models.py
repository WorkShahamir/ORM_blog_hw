from django.db import models


class AbstractUser(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)

    class Meta:
        abstract = True


class Author(AbstractUser):
    username = models.CharField(max_length=30)
    date_register = models.DateField(auto_now=True)

    def __str__(self):
        return self.username


class Article(models.Model):
    title = models.CharField(max_length=30)
    authors = models.ManyToManyField(Author, related_name="authors", through='Publication')

    def __str__(self):
        return self.title


class Publication(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    date_published = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.author} - {self.date_published} - {self.article}'
