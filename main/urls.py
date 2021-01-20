from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.blog_view, name='index'),
    path('blog/', views.blog_view, name='blog'),
    path('blog/<slug:slug>/',
         views.blog_detail, name='detail')
]
