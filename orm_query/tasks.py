import csv
from celery import shared_task
from django.core.mail import send_mail
from .models import Book, Author


@shared_task
def import_books_from_csv(file_path, user_email):
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            author, _ = Author.objects.get_or_create(name=row['author'])
            Book.objects.create(title=row['title'], author=author)

    # Надсилаємо підтвердження
    send_mail(
        'Завершення імпорту книг',
        'Імпорт книг з файлу завершено.',
        'vladislavmojseev@gmail.com.com',
        ["Vladyslav.Moiseiev@cs.khpi.edu.ua"],
        fail_silently=False,
    )
    return "Import completed successfully."