from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.indexHTML, name='index'),
    path('blog/', views.blog_view, name='blog'),
    path('blog/<str:slug>/',
         views.blog_detail, name='detail'),
    path('blog/filter/<str:type>/<str:condition>/', views.category, name='category'),
    # path('send/',views.send, name='send'),
]
