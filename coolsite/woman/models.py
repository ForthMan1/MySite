from django.db import models
from django.urls import reverse


# Create your models here.

# Пример того как можно описовать модель тоблиц в БД

class Woman(models.Model):  # Здесь мы не указали id так как в этом модуле он идет автоматический
    title = models.CharField(max_length=255 , verbose_name='Загаловок')  # CharField определяет текстовое поле
    slug = models.SlugField(max_length=255, unique=True, db_index=True,verbose_name="URL") # Чтобы отображать наши URL адресс в виде slug
    content = models.TextField(blank=True, verbose_name='Контент')  # TextField для определения текстового поля
    # blank принемает лишь 2 параметра если мы указали True то это  означает что данное поле может быть пустым
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='Фото')
    # photo будет хранить лишь путь к файлу в таблице БД, и чтобы Django мог автоматический выполнять загурзку
    # графических файлов и формиравть к ним путь нужно настроить 2 константы (MEDIA_ROOT, MEDIA_URLwW)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')  # auto_now_add туда записывается дату первый раз загрузки
    # зачастую она не меняется
    time_update = models.DateTimeField(
        auto_now=True , verbose_name='Время изменения')  # auto_now дата каждый раз перезаписывается когда мы редактируем пост
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория') # внешний ключ который мы определили ниже классом

    def __str__(self):
        return self.title

    def get_absolute_url(self):  # self - это ссылка класса Woman поэтому мы можем вызывать этот атрибут
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Знаменитые Женщины'
        verbose_name_plural = 'Знаменитые Женщины'
        ordering = ['time_create','title']


class Category(models.Model):
    # здесь id добавляется автоматический
    name = models.CharField(max_length=100, db_index=True, verbose_name="Категория")  # Название категории
    slug = models.SlugField(max_length=255, db_index=True, unique=True, verbose_name='URL')
    # max_length - указываем макс длину
    # db_index - означает что это поле будет индексированна

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})

    class Meta:
        verbose_name = 'Категории Женщин'
        verbose_name_plural = 'Категории Женщин'
        ordering = ['id']


    def __str__(self): # магический метод который возваршает имя катигорий
        return self.name
