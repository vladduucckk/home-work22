from django.urls import path
from . import views

urlpatterns = [
    path('books-deep-learning/', views.book_stats_view, name='book_stats_view_deep_learning'),
    path('row-sql/', views.row_sql, name='row_sql_view_deep_learning'),
]
