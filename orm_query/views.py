import os

from celery.result import AsyncResult
from django.shortcuts import render, redirect
import time

from productivity_orm_session_cookie import settings
from .tasks import *
from .forms import CSVUploadForm
from .models import Book, Author, Review


def compare_time_sql(request):
    if request.method == 'POST':
        # Створення авторів
        author1 = Author.objects.create(name='J.K. Rowling')
        author2 = Author.objects.create(name='George Orwell')
        author3 = Author.objects.create(name='J.R.R. Tolkien')
        author4 = Author.objects.create(name='Harper Lee')
        author5 = Author.objects.create(name='F. Scott Fitzgerald')
        author6 = Author.objects.create(name='Leo Tolstoy')
        author7 = Author.objects.create(name='Jane Austen')
        author8 = Author.objects.create(name='Mark Twain')
        author9 = Author.objects.create(name='Charles Dickens')
        author10 = Author.objects.create(name='Ernest Hemingway')
        author11 = Author.objects.create(name='Agatha Christie')
        author12 = Author.objects.create(name='William Shakespeare')
        author13 = Author.objects.create(name='Virginia Woolf')
        author14 = Author.objects.create(name='Emily Dickinson')
        author15 = Author.objects.create(name='H.G. Wells')
        author16 = Author.objects.create(name='Oscar Wilde')
        author17 = Author.objects.create(name='Jack London')
        author18 = Author.objects.create(name='Stephen King')
        author19 = Author.objects.create(name='J.D. Salinger')
        author20 = Author.objects.create(name='Isaac Asimov')

        # Створення книг
        book1 = Book.objects.create(title='Harry Potter and the Sorcerer\'s Stone', author=author1)
        book2 = Book.objects.create(title='1984', author=author2)
        book3 = Book.objects.create(title='The Hobbit', author=author3)
        book4 = Book.objects.create(title='To Kill a Mockingbird', author=author4)
        book5 = Book.objects.create(title='The Great Gatsby', author=author5)
        book6 = Book.objects.create(title='War and Peace', author=author6)
        book7 = Book.objects.create(title='Pride and Prejudice', author=author7)
        book8 = Book.objects.create(title='Adventures of Huckleberry Finn', author=author8)
        book9 = Book.objects.create(title='A Tale of Two Cities', author=author9)
        book10 = Book.objects.create(title='The Old Man and the Sea', author=author10)
        book11 = Book.objects.create(title='Murder on the Orient Express', author=author11)
        book12 = Book.objects.create(title='Romeo and Juliet', author=author12)
        book13 = Book.objects.create(title='Mrs. Dalloway', author=author13)
        book14 = Book.objects.create(title='Poems', author=author14)
        book15 = Book.objects.create(title='The War of the Worlds', author=author15)
        book16 = Book.objects.create(title='The Picture of Dorian Gray', author=author16)
        book17 = Book.objects.create(title='The Call of the Wild', author=author17)
        book18 = Book.objects.create(title='It', author=author18)
        book19 = Book.objects.create(title='The Catcher in the Rye', author=author19)
        book20 = Book.objects.create(title='Foundation', author=author20)

        # Додавання додаткових книг до кожного автора для тесту
        book21 = Book.objects.create(title='Harry Potter and the Chamber of Secrets', author=author1)
        book22 = Book.objects.create(title='Animal Farm', author=author2)
        book23 = Book.objects.create(title='The Fellowship of the Ring', author=author3)
        book24 = Book.objects.create(title='Go Set a Watchman', author=author4)
        book25 = Book.objects.create(title='Tender is the Night', author=author5)
        book26 = Book.objects.create(title='Anna Karenina', author=author6)
        book27 = Book.objects.create(title='Sense and Sensibility', author=author7)
        book28 = Book.objects.create(title='The Prince and the Pauper', author=author8)
        book29 = Book.objects.create(title='Great Expectations', author=author9)
        book30 = Book.objects.create(title='For Whom the Bell Tolls', author=author10)
        book31 = Book.objects.create(title='The ABC Murders', author=author11)
        book32 = Book.objects.create(title='Macbeth', author=author12)
        book33 = Book.objects.create(title='Orlando', author=author13)
        book34 = Book.objects.create(title='The Belle of Amherst', author=author14)
        book35 = Book.objects.create(title='The Invisible Man', author=author15)
        book36 = Book.objects.create(title='The Importance of Being Earnest', author=author16)
        book37 = Book.objects.create(title='White Fang', author=author17)
        book38 = Book.objects.create(title='The Shining', author=author18)
        book39 = Book.objects.create(title='Franny and Zooey', author=author19)
        book40 = Book.objects.create(title='I, Robot', author=author20)

        # Створення відгуків
        review1 = Review.objects.create(review='An amazing start to a magical journey!', book=book1)
        review2 = Review.objects.create(review='A chilling look into a dystopian future.', book=book2)
        review3 = Review.objects.create(review='A fantastic adventure through Middle-earth.', book=book3)
        review4 = Review.objects.create(review='A powerful message about justice and morality.', book=book4)
        review5 = Review.objects.create(review='A timeless classic about the American dream.', book=book5)
        review6 = Review.objects.create(review='An epic tale of love, war, and honor.', book=book6)
        review7 = Review.objects.create(review='A brilliant portrayal of social class and relationships.', book=book7)
        review8 = Review.objects.create(review='A humorous and insightful story of growing up.', book=book8)
        review9 = Review.objects.create(review='A masterpiece of historical fiction with deep themes.', book=book9)
        review10 = Review.objects.create(review='A short but profound exploration of life and death.', book=book10)

        # Додавання додаткових відгуків
        review11 = Review.objects.create(review='Magical and enchanting!', book=book1)
        review12 = Review.objects.create(review='An unsettling look at a totalitarian world.', book=book2)
        review13 = Review.objects.create(review='A journey of self-discovery and courage.', book=book3)
        review14 = Review.objects.create(review='A heart-wrenching story of racial injustice.', book=book4)
        review15 = Review.objects.create(review='A tragic tale of love and loss.', book=book5)
        review16 = Review.objects.create(review='An intricate story of Russian aristocracy.', book=book6)
        review17 = Review.objects.create(review='A witty critique of early 19th-century England.', book=book7)
        review18 = Review.objects.create(review='A deep dive into the human condition and the meaning of life.',
                                         book=book8)
        review19 = Review.objects.create(review='A great historical novel with unforgettable characters.', book=book9)
        review20 = Review.objects.create(review='A story of personal struggle and triumph.', book=book10)

        # Додаткові записи для відгуків
        review21 = Review.objects.create(review='Thrilling plot twists!', book=book11)
        review22 = Review.objects.create(review='A brilliant exploration of the human psyche.', book=book12)
        review23 = Review.objects.create(review='A beautiful depiction of the struggle for freedom.', book=book13)
        review24 = Review.objects.create(review='A perfect mix of mystery and action.', book=book14)
        review25 = Review.objects.create(review='A compelling dystopian narrative.', book=book15)
        review26 = Review.objects.create(review='A remarkable critique of social norms.', book=book16)
        review27 = Review.objects.create(review='Deep and evocative storytelling.', book=book17)
        review28 = Review.objects.create(review='Chillingly atmospheric.', book=book18)
        review29 = Review.objects.create(review='A masterclass in suspense.', book=book19)
        review30 = Review.objects.create(review='Poignant and emotional.', book=book20)

        # Додаткові записи до інших книг
        review31 = Review.objects.create(review='Classic and unforgettable!', book=book21)
        review32 = Review.objects.create(review='A witty satire on political systems.', book=book22)
        review33 = Review.objects.create(review='A magical fantasy masterpiece.', book=book23)
        review34 = Review.objects.create(review='A beautifully written novel about social injustice.', book=book24)
        review35 = Review.objects.create(review='An emotional, heart-wrenching story.', book=book25)
        review36 = Review.objects.create(review='A monumental work of historical fiction.', book=book26)
        review37 = Review.objects.create(review='A brilliant retelling of an old legend.', book=book27)
        review38 = Review.objects.create(review='A poetic reflection on the beauty of nature.', book=book28)
        review39 = Review.objects.create(review='A thrilling adventure that will keep you hooked.', book=book29)
        review40 = Review.objects.create(review='A chilling tale of psychological horror.', book=book30)
        start_no_opt = time.time()
        books = Book.objects.all()

        for book in books:
            print(book.title, book.author.name)
        end_no_opt = time.time() - start_no_opt
        start_opt = time.time()
        books = Book.objects.select_related('author').all()

        for book in books:
            print(book.title, book.author.name)
        end_opt = time.time() - start_opt
        return render(request, 'compare_sql_time.html', context={'no_opt': end_no_opt, "opt": end_opt})
    else:
        return render(request, 'compare_sql_time.html')


from django.shortcuts import render
from django.core.cache import cache
from .models import Book


# Відображення для списку книг
def book_list_view(request):
    # Перевіряємо, чи є кеш для списку книг
    cached_books = cache.get('book_list')

    if not cached_books:
        # Якщо кеш відсутній, отримуємо книги з бази даних
        books = Book.objects.select_related('author').all()

        # Кешуємо результат на 60 секунд
        cache.set('book_list', books, timeout=60)
    else:
        books = cached_books

    return render(request, 'book_list.html', {'books': books})


def upload_csv_view(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = form.cleaned_data['csv_file']
            file_path = os.path.join(settings.MEDIA_ROOT, csv_file.name)

            # Зберігаємо файл
            with open(file_path, 'wb+') as destination:
                for chunk in csv_file.chunks():
                    destination.write(chunk)

            # Перевіряємо, чи користувач авторизований перед відправкою email
            user_email = request.user.email if request.user.is_authenticated else "vladislavmojseev@gmail.com"

            # Запускаємо завдання Celery
            task = import_books_from_csv.delay(file_path, user_email)

            return redirect('task_status', task_id=task.id)
    else:
        form = CSVUploadForm()

    return render(request, 'upload_csv.html', {'form': form})

def task_status_view(request, task_id):
    result = AsyncResult(task_id)
    return render(request, 'task_status.html', {'result': result})