from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *


# Create your views here.
def index(request):
    posts = Woman.objects.all()
    context = {
        'posts': posts,
        'title': 'Main page',
        'cat_selected': 0,  # 0 - чтобы на главной стр отображались все записи
    }
    return render(request, 'woman/index.html', context=context)


def about_site(requests):
    context = {
        'title': 'О нас кой',
    }
    return render(requests, 'woman/about_sites.html', context=context)


def catigories(request, cat):
    return HttpResponse("<h1>Hello, beach</h1>"
                        f"<b>cat id is: {cat}</b>")


def archive(request, year):
    if int(year) > 2022:
        return redirect('home', permanent=True)

    return HttpResponse("<h1>Hello, whats up?</h1>"
                        f"<b>year you are wrote is : {year}</b>")


def contents(request):
    if request.method == 'POST':
        form = ContentsForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            try:
                Woman.objects.create(**form.cleaned_data)
                return redirect('home')
            except:
                form.add_error(None, 'Ошибка при добовлении в БД')
    else:
        form = ContentsForm()
    context = {
        'title': 'This is content side',
        'form': form,
    }
    return render(request, 'woman/contents.html', context=context)


def contacts(requests):
    context = {
        'title': 'Our Contacts',
    }
    return render(requests, 'woman/contact.html', context=context)


def login(requests):
    context = {
        'title': 'Sign in',
    }
    return render(requests, 'woman/sign_in.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")


def show_post(request, post_slug):
    posts = get_object_or_404(Woman, slug=post_slug)
    context = {
        'posts': posts,
        'title': posts.title,
        'cat_selected': posts.cat_id  # здесь так же можно просто поставить "1"
    }
    return render(request, 'woman/post.html', context=context)


def show_category(request, cat_id):
    posts = Woman.objects.filter(cat_id=cat_id)  # мы здесь выбираем не все посты, только те которые нам нужны

    if len(posts) == 0:  # если запись на стр будет пуста выведит окно 404
        raise Http404()

    context = {  # передаем все те же данные что и в функции index
        'posts': posts,
        'title': 'По рубрикам',
        'cat_selected': cat_id,  # cat_id - передаем переменную которую прочитали из запроса
    }
    return render(request, 'woman/index.html', context=context)
