from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('free_board/', views.free_board, name='free_board'),
    path('question_board/', views.question_board, name='question_board'),
    path('concern_board/', views.concern_board, name='concern_board'),
    path('edu_board/', views.edu_board, name='edu_board'),
    path('know_how_board/', views.know_how_board, name='know_how_board'),
    path('mypage/', views.mypage, name='mypage'),
    path('login/', views.login, name='login'),
    path('question_write_page/', views.question_write_page, name='question_write_page'),
]
