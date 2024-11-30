from django.shortcuts import render
from django.db.models import Count, Avg
from django.shortcuts import render
from .models import Author_2, Book_2, Review_2


def book_stats_view(request):
    # Підрахунок середнього рейтингу для кожної книги
    # Підрахунок кількості відгуків для кожної книги
    books_2 = Book_2.objects.annotate(
        avg_rating=Avg('review_2__rating'),  # Середній рейтинг
        review_count=Count('review_2')  # Кількість відгуків
    ).order_by('-review_count', '-avg_rating')  # Сортування за кількістю відгуків та рейтингом

    # Підрахунок середнього рейтингу для кожного автора
    authors_2 = Author_2.objects.annotate(
        avg_author_rating=Avg('book_2__review_2__rating')  # Середній рейтинг книг автора
    )

    context = {
        'books_2': books_2,
        'authors_2': authors_2,
    }
    return render(request, 'book_stats_2.html', context)


def row_sql(request):
    # підрахунки загальної кількості книг
    total_books = Book_2.objects.raw("SELECT COUNT(*) as data, 1 as id FROM deep_learning_sql_book_2")
    # Автори які мають книги більш ніж з 10 відгуками
    query = """
            SELECT a.id, a.name
            FROM deep_learning_sql_author_2 a
            JOIN deep_learning_sql_book_2 b ON a.id = b.author_id
            JOIN deep_learning_sql_review_2 r ON b.id = r.book_id
            GROUP BY a.id, a.name
            HAVING COUNT(r.id) > 10
        """
    authors = Author_2.objects.raw(query)

    return render(request, 'row.sql.html', context={'total_books': total_books[0].data, 'authors': authors})
