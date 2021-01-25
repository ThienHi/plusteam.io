from django.urls import path
from . import views

urlpatterns = [
    path('',views.hire, name='hire'),
    path("<int:question_id>/", views.vote, name="vote"),
]