from django import template
from woman.models import *

register = template.Library()  # экзепляр класса Library через который происходит регитрац. собсвтенных шаблонных тегов


@register.simple_tag(name='getcats')  # мы должны эту функцию сделать простим тегом для этог прописывакм этот декоратор
def get_categories():  # пропишим функцию для работы простого тега
    return Category.objects.all()


@register.inclusion_tag('woman/list_categories.html')  # создаем включаюший тег
def show_categories(sort=None, cat_selected=0):
    if not sort:
        cats = Category.objects.all()
    else:
        cats = Category.objects.order_by(sort)

    return {"cats": cats, "cat_selected": cat_selected}


@register.inclusion_tag('woman/Main_menu.html')  # здесь мы переопределили наше меню
def show_menu():
    menu = [
        {'title': "О сайте", 'url_name': 'about_us'},
        {'title': "Добавить статью", 'url_name': 'add_content'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'sign_in'},
    ]
    return {'menu': menu}
