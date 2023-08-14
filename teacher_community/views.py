from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.utils import timezone
from .forms import SignupForm
from .models import Post

def main(request):
    posts = Post.objects.all()
    return render(request, 'main.html', {'posts':posts})

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

def free_board(request):
    posts = Post.objects.filter(category='자유게시판')
    return render(request, 'free_board.html', {'posts':posts})

def free_detail(request, post_id):
    post_detail = get_object_or_404(Post, pk = post_id)
    return render(request, 'free_detail.html', {'post_detail':post_detail})

def free_write_page(request):
    return render(request, 'free_write_page.html')

def create_post(request):
    post = Post()
    post.title = request.POST['title']
    post.author = request.user
    post.content = request.POST['content']
    post.category = request.POST['category']
    post.created_at = timezone.datetime.now()
    post.updated_at = timezone.datetime.now()
    post.save()
    return render(request, 'main.html')

def update_post(request, post_id):
    post = Post.objects.get(id=post_id)
    post.title = request.POST['title']
    post.content = request.POST['content']
    post.updated_at = timezone.datetime.now()
    post.save()
    return render(request, 'main.html')

def delete_post(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return render(request, 'main.html')

def question_board(request):
    return render(request, 'question_board.html')

def concern_board(request):
    return render(request, 'concern_board.html')

def edu_board(request):
    return render(request, 'edu_board.html')

def know_how_board(request):
    return render(request, 'know-how_board.html')

def mypage(request):
    return render(request, 'mypage.html')


def question_write_page(request):

    return render(request, 'question_write_page.html')

def concern_write_page(request):
    return render(request, 'concern_write_page.html')

def edu_write_page(request):
    return render(request, 'edu_write_page.html')

def know_how_write_page(request):
    return render(request, 'know-how_write_page.html')

# def join(request):
#     return render(request, 'join.html')

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
