from django.shortcuts import render

def main(request):
    return render(request, 'main.html')

def free_board(request):
    return render(request, 'free_board.html')

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
