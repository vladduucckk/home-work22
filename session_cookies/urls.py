from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('greeting/', views.greeting_view, name='greeting'),
    path('logout/', views.logout_view, name='logout'),
]
