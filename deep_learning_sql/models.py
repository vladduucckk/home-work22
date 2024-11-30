from django.db import models


class Author_2(models.Model):
    name = models.CharField(max_length=100, db_index=True)


class Book_2(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    author = models.ForeignKey(Author_2, on_delete=models.CASCADE)


class Review_2(models.Model):
    review = models.TextField()
    rating = models.IntegerField(db_index=True)  # Додаємо поле для оцінки
    book = models.ForeignKey(Book_2, on_delete=models.CASCADE)
