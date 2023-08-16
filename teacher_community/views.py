from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .forms import SignupForm
from .models import Post, Comment
from .models import AttachedFile
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse

from django.http import JsonResponse
from .models import Teacher

from .forms import PostForm

def main(request):
    posts = Post.objects.all()
    return render(request, 'main.html', {'posts':posts})

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

def check_username(request):
    if request.method == "GET":
        username = request.GET.get("username")
        exists = Teacher.objects.filter(username=username).exists()
        return JsonResponse({"exists": exists})

@login_required
def mypage(request):
    
    user = request.user
    my_posts = Post.objects.filter(author=user)
    my_comments = Comment.objects.filter(author=user)     

    context = {
        'user': user,
        'my_posts': my_posts,
        'my_comments': my_comments,
    }

    return render(request, 'mypage.html', context)

###free###
def free_board(request):
    posts = Post.objects.filter(category='free')
    return render(request, 'free_board.html', {'posts': posts})

def free_search(request):
    query = request.GET.get('q')  # 검색어를 가져옴


    if query:
        # 제목에 검색어가 포함된 게시물을 필터링하여 가져옴
        posts = Post.objects.filter(category='free', title__contains=query)
    else:
        posts = Post.objects.none()  # 빈 쿼리셋 반환

    context = {
        'search_results': posts,
    }
    return render(request, 'free_search.html', context)

def free_board(request):
    return render(request, 'free_board.html')


def free_write(request):
    return render(request, 'free_write.html')

def free_modify(request, post_id):
    post_detail = get_object_or_404(Post, pk = post_id)
    return render(request, 'free_modify.html', {'post_detail':post_detail})

###question###
def question_board(request):
    posts = Post.objects.filter(category='question')
    return render(request, 'question_board.html', {'posts': posts})

def question_search(request):
    query = request.GET.get('q')  # 검색어를 가져옴

    if query:
        # 제목에 검색어가 포함된 게시물을 필터링하여 가져옴
        posts = Post.objects.filter(category='question', title__contains=query)
    else:
        posts = Post.objects.none()  # 빈 쿼리셋 반환

    context = {
        'search_results': posts,
    }
    return render(request, 'question_search.html', context)

def question_write(request):
    return render(request, 'question_write.html')

def question_modify(request, post_id):
    post_detail = get_object_or_404(Post, pk = post_id)
    return render(request, 'question_modify.html', {'post_detail':post_detail})

###concern###
def concern_board(request):
    posts = Post.objects.filter(category='concern')
    return render(request, 'concern_board.html', {'posts': posts})

def concern_search(request):
    query = request.GET.get('q')  # 검색어를 가져옴

    if query:
        # 제목에 검색어가 포함된 게시물을 필터링하여 가져옴
        posts = Post.objects.filter(category='concern', title__contains=query)
    else:
        posts = Post.objects.none()  # 빈 쿼리셋 반환

    context = {
        'search_results': posts,
    }
    return render(request, 'concern_search.html', context)

def concern_write(request):
    return render(request, 'concern_write.html')

def concern_modify(request, post_id):
    post_detail = get_object_or_404(Post, pk = post_id)
    return render(request, 'concern_modify.html', {'post_detail':post_detail})

###edu###
def edu_board(request):
    posts = Post.objects.filter(category='edu')
    return render(request, 'edu_board.html', {'posts': posts})

def edu_search(request):
    query = request.GET.get('q')  # 검색어를 가져옴

    if query:
        # 제목에 검색어가 포함된 게시물을 필터링하여 가져옴
        posts = Post.objects.filter(category='edu', title__contains=query)
    else:
        posts = Post.objects.none()  # 빈 쿼리셋 반환

    context = {
        'search_results': posts,
    }
    return render(request, 'edu_search.html', context)

def edu_write(request):
    return render(request, 'edu_write.html')

def edu_detail(request, post_id):
    post_detail = get_object_or_404(Post, pk=post_id)
    return render(request, 'edu_detail.html', {'post_detail': post_detail})

def edu_modify(request, post_id):
    post_detail = get_object_or_404(Post, pk = post_id)
    return render(request, 'edu_modify.html', {'post_detail':post_detail})

###know-how###
def know_how_board(request):
    posts = Post.objects.filter(category='know-how')
    return render(request, 'know-how_board.html', {'posts': posts})

def know_how_search(request):
    query = request.GET.get('q')  # 검색어를 가져옴

    if query:
        # 제목에 검색어가 포함된 게시물을 필터링하여 가져옴
        posts = Post.objects.filter(category='know-how', title__contains=query)
    else:
        posts = Post.objects.none()  # 빈 쿼리셋 반환

    context = {
        'search_results': posts,
    }
    return render(request, 'know-how_search.html', context)

def know_how_write(request):
    return render(request, 'know-how_write.html')

def know_how_modify(request, post_id):
    post_detail = get_object_or_404(Post, pk = post_id)
    return render(request, 'know-how_modify.html', {'post_detail':post_detail})

def detail(request, post_id):
    post_detail = get_object_or_404(Post, pk=post_id)

    # 게시물 조회 시 조회수 증가
    post_detail.increase_views()

    return render(request, 'detail.html', {'post_detail': post_detail})


def create_post(request):
    post = Post()
    post.title = request.POST['title']
    post.author = request.user
    post.content = request.POST['content']
    post.category = request.POST['category']
    post.created_at = timezone.datetime.now()
    post.updated_at = timezone.datetime.now()
    post.save()
    return redirect('/detail/' + str(post.id))

# def update_post(request, post_id):
#     post = Post.objects.get(id=post_id)
#     post.title = request.POST['title']
#     post.content = request.POST['content']
#     post.updated_at = timezone.datetime.now()
#     post.save()
#     return render(request, 'main.html')





def update_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect(f'{post.category}_board')
    else:
        form = PostForm(instance=post)
    
    return render(request, 'update_post.html', {'form': form, 'post': post})





def delete_post(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return render(request, 'main.html')

def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    user = request.user

    if user.is_authenticated:
        liked_posts = user.like_set.all()
        if post in liked_posts:
            user.like_set.remove(post)
        else:
            user.like_set.add(post)

        post_likes_count = post.like_set.count()  # 해당 포스트의 좋아요 수 계산
        user_like_count = user.like_set.count()  # 사용자별 좋아요 수 계산
        return JsonResponse({'post_likes_count': post_likes_count, 'user_like_count': user_like_count})

    return JsonResponse({}, status=401)  # 인증되지 않은 사용자에게는 401 Unauthorized 응답

