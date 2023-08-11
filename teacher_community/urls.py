from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('concern_board/', views.concern_board, name='concern_board'),
    path('concern_write_page/', views.concern_write_page, name='concern_write_page'),
    path('edu_board/', views.edu_board, name='edu_board'),
    path('edu_write_page/', views.edu_write_page, name='edu_write_page'),
    path('free_board/', views.free_board, name='free_board'),
    path('free_write_page/', views.free_write, name='free_write_page'),
    path('issue/', views.issue, name='issue'),
    path('join/', views.join, name='join'),
    path('know_how_board/', views.know_how_board, name='know_how_board'),
    path('know_how_write_page/', views.know_how_write_page, name='know_how_write_page'),
    path('login/', views.login, name='login'),
    path('main/', views.main, name='main'),
    path('mypage/', views.mypage, name='mypage'),
    path('question_board/', views.question_board, name='question_board'),
    path('question_write_page/', views.question_write_page, name='question_write_page'),
]


