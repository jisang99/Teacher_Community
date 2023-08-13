from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .forms import SignupForm

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

# def join(request):
#     return render(request, 'join.html')

def issue(request):
    return render(request, 'issue.html')

# 로그인
# def login(request):
#     return render(request, 'login.html')

def login_view(request):
    form = AuthenticationForm(request=request, data=request.POST)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(request=request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form':form})
    
def logout_view(request):
    logout(request)
    return redirect('main')


def join_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)  # 가입 후 자동 로그인
            return redirect('main')  # 회원가입 완료 후 이동할 페이지
    else:
        form = SignupForm()
        print(form.errors)

    return render(request, 'join.html', {'form': form})
