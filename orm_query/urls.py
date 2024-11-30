from django.urls import path
from . import views

urlpatterns = [
    path('compare-time-sql/', views.compare_time_sql, name='compare-sql'),
    path('books/', views.book_list_view, name='books'),
    path('upload/', views.upload_csv_view, name='upload_csv'),
    path('task_status/<task_id>/', views.task_status_view, name='task_status'),
]
