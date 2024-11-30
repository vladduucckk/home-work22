from django.shortcuts import render, redirect
from .forms import LoginForm


# Функція для оновлення cookies
def update_cookie(response, name, value, max_age=3600):
    response.set_cookie(name, value, max_age=max_age)  # Використовуємо тільки max_age


# Обробник форми входу
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # Отримуємо дані з форми
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']

            # Зберігаємо дані у cookies та сесії
            response = redirect('greeting')
            response.set_cookie('name', name, max_age=3600)  # Зберігаємо на 1 годину
            request.session['age'] = age
            return response
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


# Обробник сторінки привітання
def greeting_view(request):
    name = request.COOKIES.get('name')
    age = request.session.get('age')

    if not name or not age:
        return redirect('login')

    # Автоматичне подовження cookies
    response = render(request, 'greeting.html', {'name': name, 'age': age})
    update_cookie(response, 'name', name)  # Подовжуємо cookies
    return response


# Обробник виходу (очищення cookies та сесії)
def logout_view(request):
    response = redirect('login')
    response.delete_cookie('name')
    request.session.flush()  # Очищає всю сесію
    return response
