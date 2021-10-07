from django.urls import path, re_path
from django.conf.urls import url
from . import views
from blog import views as article_views

app_name = 'blog'

urlpatterns = [
    path('', article_views.article, name='home'),
    path('about/', views.about, name='about'),
    path('article/', views.article, name='article'),
    # slug url setting
    path('create/', views.create_view, name='create'),
    re_path(r'^(?P<slug>[\w-]+)/$', views.article_details, name='details'),
]