from django.shortcuts import render
from .forms import UserRegister
from .models import Buyer, Game, News
from django.core.paginator import Paginator

def news(request):
    news_list = News.objects.all().order_by('-date')
    paginator = Paginator(news_list, 5)
    page_number = request.GET.get('page')
    news = paginator.get_page(page_number)

    context = {
        'title': 'Новости',
        'menu': {'platform': '/',
                 'games': '/games/',
                 'cart': '/cart/',
                 'news': '/platform/news/'},
        'news': news
    }
    return render(request, 'fourth_task/news.html', context)
def platform(request):
    context = {
        'title': 'Игровая платформа',
        'menu': {'platform': '/',
                 'games': '/games/',
                 'cart': '/cart/'},
        'content': ''
    }
    return render(request, 'fourth_task/platform.html', context)
def games(request):
    games = Game.objects.all()
    context = {
        'title': 'Игры',
        'menu': {'platform': '/',
                 'games': '/games/',
                 'cart': '/cart/'},
        'games': games
    }
    return render(request, 'fourth_task/games.html', context)
def cart(request):
    context = {
        'title': 'Корзина',
        'menu': {'platform': '/',
                 'games': '/games/',
                 'cart': '/cart/'},
        'content': 'Ваша корзина сейчас пуста'
    }
    return render(request, 'fourth_task/cart.html', context)

def sign_up_by_django(request):
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            if not Buyer.objects.filter(name=username).exists():
                Buyer.objects.create(
                    name=username,
                    balance=0,
                    age=form.cleaned_data['age']
                )
                return render(request, 'fifth_task/registration_page.html', {'message': f'Приветствуем, {username}!'})
            else:
                return render(request, 'fifth_task/registration_page.html', {'error': 'Пользователь с таким именем уже существует'})
    else:
        form = UserRegister()
    return render(request, 'fifth_task/registration_page.html', {'form': form})

def sign_up_by_html(request):
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            if not Buyer.objects.filter(name=username).exists():
                Buyer.objects.create(
                    name=username,
                    balance=0,
                    age=form.cleaned_data['age']
                )
                return render(request, 'fifth_task/registration_page.html', {'message': f'Приветствуем, {username}!'})
            else:
                return render(request, 'fifth_task/registration_page.html',
                              {'error': 'Пользователь с таким именем уже существует'})
    else:
        form = UserRegister()
        return render(request, 'fifth_task/registration_page.html', {'form': form})


