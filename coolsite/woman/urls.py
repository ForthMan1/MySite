from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('cats/<slug:cat>/', catigories, name='catigories'),
    re_path(r'^archive/(?P<year>[0-9]{4})', archive, name='archive'),
    path('about_us/', about_site, name='about_us'),
    path('add_content/', contents, name='add_content'),
    path('contact/', contacts, name='contact'),
    path('sign_in/', login, name='sign_in'),
    path('post/<slug:post_slug>/', show_post, name = 'post'),
    path('category/<int:cat_id>',show_category, name = 'category'),
]
