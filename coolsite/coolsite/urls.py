"""coolsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from coolsite import settings
from woman.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('woman.urls')),
]
# в настояших серваках это все будет настроено
if settings.DEBUG: # режиме отладке когда у нас DEBUG имеет значение True
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    # мы к моршрутам urlpatterns(они пропиманы выше), добавляем еще один марщрут статичисекие данные грф. файлов
    # сперва указываем URL (settings.MEDIA_URL) затем указываем корневую папку  (document_root = settings.MEDIA_ROOT)
    # Где непосредственно находятся наши граф. файлы (Все это делает только в отладочном режиме)


handler404 = pageNotFound
