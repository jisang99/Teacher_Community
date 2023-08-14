from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('concern_board/', views.concern_board, name='concern_board'),
    path('concern_write_page/', views.concern_write_page, name='concern_write_page'),
    path('edu_board/', views.edu_board, name='edu_board'),
    path('edu_write_page/', views.edu_write_page, name='edu_write_page'),
    path('free_board/', views.free_board, name='free_board'),
    path('free_write_page/', views.free_write_page, name='free_write_page'),
    path('create_post/', views.create_post, name='create_post'),
    path('update_post/<int:post_id>', views.update_post, name='update_post'),
    path('delete_post/<int:post_id>', views.delete_post, name='delete_post'),
    path('free_detail/<int:post_id>', views.free_detail, name='free_detail'),
    path('join/', views.join_view, name='join'),
    path('know-how_board/', views.know_how_board, name='know-how_board'),
    path('know-how_write_page/', views.know_how_write_page, name='know-how_write_page'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('main/', views.main, name='main'),
    path('mypage/', views.mypage, name='mypage'),
    path('question_board/', views.question_board, name='question_board'),
    path('question_write_page/', views.question_write_page, name='question_write_page'),
    path('free_board_search/', views.free_board_search, name='free_board_search'),
    path('question/<int:post_id>/', views.question_detail, name='question_detail'),
    path('concern/<int:post_id>/', views.concern_detail, name='concern_detail'),
    path('edu_detail/<int:post_id>/', views.edu_detail, name='edu_detail'),
]