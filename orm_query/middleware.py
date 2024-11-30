from django.core.cache import cache
from django.http import HttpResponse


class CachePageForAnonymousUsersMiddleware:
    """Кешування для анонімних користувачів"""
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path == '/books/':
            # Якщо користувач анонімний
            if not request.user.is_authenticated:
                # Перевіряємо наявність кешованої сторінки
                cached_page = cache.get('book_list_page')
                if cached_page:
                    return HttpResponse(cached_page)

        response = self.get_response(request)

        # Кешуємо сторінку для анонімних користувачів
        if request.path == '/books/' and not request.user.is_authenticated:
            cache.set('book_list_page', response.content, timeout=60)

        return response