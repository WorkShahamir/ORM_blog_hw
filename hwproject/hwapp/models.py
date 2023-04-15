from django.db import models


class AbstractAccount(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    class Meta:
        abstract = True


class Author(AbstractAccount):
    username = models.CharField(max_length=255)
    date_register = models.DateField()

    def __str__(self):
        return self.username


class Article(models.Model):
    title = models.CharField(max_length=255)
    author = models.ManyToManyField(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.author


class Publication(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    date_published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.article} - {self.author}"

