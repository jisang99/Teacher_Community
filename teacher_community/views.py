from django.shortcuts import render
from .models import Post  # 필요한 모델 임포트

def main(request):
    return render(request, 'main.html')

def free_board(request):
    return render(request, 'free_board.html')

def free_board_search(request):
    query = request.GET.get('q')  # 검색어를 가져옴

    if query:
        # 제목에 검색어가 포함된 게시물을 필터링하여 가져옴
        posts = Post.objects.filter(title__contains=query)
    else:
        posts = []  # 검색어가 없으면 빈 리스트를 할당

    context = {
        'posts': posts,
    }

    return render(request, 'free_board_search.html', context)

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

def free_write_page(request):
    return render(request, 'free_write_page.html')

def know_how_write_page(request):
    return render(request, 'know_how_write_page.html')

def join(request):
    return render(request, 'join.html')

def issue(request):
    return render(request, 'issue.html')