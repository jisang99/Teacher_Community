from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('main/', views.main, name='main'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('join/', views.join_view, name='join'),
    path('mypage/', views.mypage, name='mypage'),

    path('free_board/', views.free_board, name='free_board'),
    path('free_search/', views.free_search, name='free_search'),
    path('free_write/', views.free_write, name='free_write'),
    path('free_modify/<int:post_id>', views.free_modify, name='free_modify'),

    path('question_board/', views.question_board, name='question_board'),
    path('question_search/', views.question_search, name='question_search'),
    path('question_write/', views.question_write, name='question_write'),
    path('question_modify/<int:post_id>', views.question_modify, name='question_modify'),

    path('concern_board/', views.concern_board, name='concern_board'),
    path('concern_search/', views.concern_search, name='concern_search'),
    path('concern_write/', views.concern_write, name='concern_write'),
    path('concern_modify/<int:post_id>/', views.concern_modify, name='concern_modify'),

    path('edu_board/', views.edu_board, name='edu_board'),
    path('edu_search/', views.edu_search, name='edu_search'),
    path('edu_write/', views.edu_write, name='edu_write'),
    path('edu_modify/<int:post_id>/', views.edu_modify, name='edu_modify'),
    
    path('know-how_board/', views.know_how_board, name='know-how_board'),
    path('know-how_search/', views.know_how_search, name='know-how_search'),
    path('know-how_write/', views.know_how_write, name='know-how_write'),
    path('know-how_modify/<int:post_id>/', views.know_how_modify, name='know_how_modify'),

    path('create_post/', views.create_post, name='create_post'),
    path('detail/<int:post_id>', views.detail, name='detail'),
    path('update_post/<int:post_id>', views.update_post, name='update_post'),
    path('delete_post/<int:post_id>', views.delete_post, name='delete_post'),
    path('like/<int:post_id>/', views.like_post, name='like_post'),
    path('check_username/', views.check_username, name='check_username'),
]