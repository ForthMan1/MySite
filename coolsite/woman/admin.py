from django.contrib import admin
from .models import *


class WomanAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'title', 'time_create', 'photo', 'is_published')  # список полей которые мы хотим видеть в нащей админке
    list_display_links = ('id', 'title')  # те поля на которые мы можем переидти как по ссылке
    search_fields = ('title', 'content')  # по каким полям можно производить поиск
    list_editable = ('is_published',)  # задаем те поля которые мы можем редактировать
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {"slug": ('title',)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ('name',)}


admin.site.register(Woman, WomanAdmin)  # указываем ту модель которую хотим зарегать
admin.site.register(Category, CategoryAdmin)
