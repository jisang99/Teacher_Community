from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.utils import timezone

def main(request):
    posts = Post.objects.all()
    return render(request, 'main.html', {'posts':posts})

def question_board(request):
    return render(request, 'question_board.html')

def concern_board(request):
    return render(request, 'concern_board.html')

def edu_board(request):
    return render(request, 'edu_board.html')

def know_how_board(request):
    return render(request, 'know_how_board.html')

def mypage(request):
    return render(request, 'mypage.html')

def login(request):
    return render(request, 'login.html')

def question_write_page(request):
    return render(request, 'question_write_page.html')

def concern_write_page(request):
    return render(request, 'concern_write_page.html')

def edu_write_page(request):
    return render(request, 'edu_write_page.html')

def free_board(request, post_id):
    post_free_board = get_object_or_404(Post, pk = post_id)
    return render(request, 'free_board.html', {'post_free_board' : post_free_board})

def free_write(request):
    if request.method=='POST':
        post = Post()
        post.title = request.GET['title']
        post.content = request.GET['content']
        post.created_at = request.GET['created_at']
        post.updated_at = request.GET['updated_at']
        post.views = request.GET['views']
        post.category = request.GET['category']
        post.save()
        return redirect('/free_board/' +str(post.id))
    else:
        return render(request, 'free_write_page.html')

def free_write_update(request, post_id):
    post - Post.objects.get(id=post_id)
    if request.method=='POST':
        post = Post()
        post.title = request.GET['title']
        post.content = request.GET['content']
        post.created_at = request.GET['created_at']
        post.updated_at = request.GET['updated_at']
        post.views = request.GET['views']
        post.category = request.GET['category']
        post.save()
        return redirect('/free_board/' +str(post.id))
    else:
        return render(request, 'free_write_page.html', {'post':post})


def know_how_write_page(request):
    return render(request, 'know_how_write_page.html')

def join(request):
    return render(request, 'join.html')

def issue(request):
    return render(request, 'issue.html')