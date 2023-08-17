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

from django.contrib import messages
from django.http import JsonResponse
from .models import Teacher

from .forms import PostForm





def login_view(request):
    form = AuthenticationForm()
    # 사용자가 실제 로그인하고 요청 보낼 때 오는 로직
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)

        # 사용자가 아이디와 비밀번호를 올바르게 쳤을 때
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request=request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("main")

        # 폼을 잘못입력했을 때
        else:
            print("에러2")
            form = AuthenticationForm()
            return render(request, "login.html", {"form": form, "display": "block"})

    # 사용자가 단순히 로그인 홈페이지에 접속할 땐 나오는 로직
    return render(request, "login.html", {"form": form, "display": "none"})


def logout_view(request):
    logout(request)
    return redirect("main")


def join_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)  # 가입 후 자동 로그인
            return redirect("main")  # 회원가입 완료 후 이동할 페이지
    else:
        form = SignupForm()
        print(form.errors)
    return render(request, "join.html", {"form": form})


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
        "user": user,
        "my_posts": my_posts,
        "my_comments": my_comments,
    }

    return render(request, "mypage.html", context)


###free###
def free_board(request):
    posts = Post.objects.filter(category="자유게시판")
    print("실행1")
    return render(request, "free_board.html", {"posts": posts})


def free_search(request):
    print("실행2")
    query = request.GET.get("q")  # 검색어를 가져옴

    if query:
        # 제목에 검색어가 포함된 게시물을 필터링하여 가져옴
        posts = Post.objects.filter(category="자유게시판", title__contains=query)
    else:
        posts = Post.objects.none()  # 빈 쿼리셋 반환

    context = {
        "search_results": posts,
    }
    return render(request, "free_search.html", context)


def free_write(request):
    return render(request, "free_write.html")


###question###
def question_board(request):
    posts = Post.objects.filter(category="질문게시판")
    return render(request, "question_board.html", {"posts": posts})


def question_search(request):
    query = request.GET.get("q")  # 검색어를 가져옴

    if query:
        # 제목에 검색어가 포함된 게시물을 필터링하여 가져옴
        posts = Post.objects.filter(category="질문게시판", title__contains=query)
    else:
        posts = Post.objects.none()  # 빈 쿼리셋 반환

    context = {
        "search_results": posts,
    }
    return render(request, "question_search.html", context)


def question_write(request):
    return render(request, "question_write.html")


###concern###
def concern_board(request):
    posts = Post.objects.filter(category="고민게시판")
    return render(request, "concern_board.html", {"posts": posts})


def concern_search(request):
    query = request.GET.get("q")  # 검색어를 가져옴

    if query:
        # 제목에 검색어가 포함된 게시물을 필터링하여 가져옴
        posts = Post.objects.filter(category="고민게시판", title__contains=query)
    else:
        posts = Post.objects.none()  # 빈 쿼리셋 반환

    context = {
        "search_results": posts,
    }
    return render(request, "concern_search.html", context)


def concern_write(request):
    return render(request, "concern_write.html")


###edu###
def edu_board(request):
    posts = Post.objects.filter(category="교육자료")
    return render(request, "edu_board.html", {"posts": posts})


def edu_search(request):
    query = request.GET.get("q")  # 검색어를 가져옴

    if query:
        # 제목에 검색어가 포함된 게시물을 필터링하여 가져옴
        posts = Post.objects.filter(category="교육자료", title__contains=query)
    else:
        posts = Post.objects.none()  # 빈 쿼리셋 반환

    context = {
        "search_results": posts,
    }
    return render(request, "edu_search.html", context)


def edu_write(request):
    return render(request, "edu_write.html")


###know-how###
def know_how_board(request):
    posts = Post.objects.filter(category="노하우")
    return render(request, "know-how_board.html", {"posts": posts})


def know_how_search(request):
    query = request.GET.get("q")  # 검색어를 가져옴

    if query:
        # 제목에 검색어가 포함된 게시물을 필터링하여 가져옴
        posts = Post.objects.filter(category="노하우", title__contains=query)
    else:
        posts = Post.objects.none()  # 빈 쿼리셋 반환

    context = {
        "search_results": posts,
    }
    return render(request, "know-how_search.html", context)


def know_how_write(request):
    return render(request, "know-how_write.html")


def detail(request, post_id):
    post_detail = get_object_or_404(Post, pk=post_id)
    comments = Comment.objects.filter(post=post_detail)
    likes_count = post_detail.count_likes_user()
    isLiked = post_detail.likes_user.filter(id=request.user.id).exists()

    # 게시물 조회 시 조회수 증가
    post_detail.increase_views()

    return render(
        request, "detail.html", {"post_detail": post_detail, "comments": comments, "likes_count": likes_count, "isLiked": isLiked}
    )


def create_post(request):
    if request.method == "POST":
        post = Post()
        post.title = request.POST["title"]
        post.author = request.user
        post.content = request.POST["content"]
        post.category = request.POST["category"]
        post.created_at = timezone.datetime.now()
        post.updated_at = timezone.datetime.now()

        if "file" in request.FILES:
            post.file = request.FILES["file"]

        post.save()

        return redirect("/detail/" + str(post.id))
    return render(request, "create_post.html")  # POST 요청이 아닌 경우에도 처리하기 위해 렌더링


# def update_post(request, post_id):
#     post = Post.objects.get(id=post_id)
#     post.title = request.POST['title']
#     post.content = request.POST['content']
#     post.updated_at = timezone.datetime.now()
#     post.save()
#     return render(request, 'main.html')



def update_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == "POST":
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.updated_at = timezone.datetime.now()
        post.save()
        return redirect('/detail/' + str(post.id))
    else:
        return render(request, "update_post.html", {"post_detail": post})


def delete_post(request, post_id):
    post = Post.objects.get(id=post_id)
    if post.category == "자유게시판":
        post.delete()
        return redirect('free_board')
    elif post.category == "질문게시판":
        post.delete()
        return redirect('question_board')
    elif post.category == "고민게시판":
        post.delete()
        return redirect('concern_board')
    elif post.category == "교육자료":
        post.delete()
        return redirect('edu_board')
    if post.category == "노하우":
        post.delete()
        return redirect('konw-how_board')


# def like_post(request, post_id):
#     post = get_object_or_404(Post, id=post_id)
#     user = request.user

#     if user.is_authenticated:
#         liked_posts = user.like_set.all()
#         if post in liked_posts:
#             user.like_set.remove(post)
#         else:
#             user.like_set.add(post)

#         post_likes_count = post.like_set.count()  # 해당 포스트의 좋아요 수 계산
#         user_like_count = user.like_set.count()  # 사용자별 좋아요 수 계산
#         return JsonResponse(
#             {"post_likes_count": post_likes_count, "user_like_count": user_like_count}
#         )

#     return JsonResponse({}, status=401)  # 인증되지 않은 사용자에게는 401 Unauthorized 응답


"""
댓글 관련 함수들
"""


def create_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    user = request.user
    print(request.user)
    comment = Comment(
        post=post,
        author=user,
        body=request.POST["body"],
    )

    comment.save()
    print("성공")

    return redirect(f"/detail/{post_id}")


def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    post_id = comment.post.id
    comment.delete()
    return redirect(f"/detail/{post_id}")

"""
좋아요 관련 함수들
"""
@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    user = request.user

    if post.likes_user.filter(id=user.id).exists():
        post.likes_user.remove(user)
        message = "좋아요 취소"
    else:
        post.likes_user.add(user)
        message = "좋아요"





def main(request):
    concern_posts = Post.objects.filter(category='고민게시판').order_by('-views')[:5]
    hot_posts = Post.objects.order_by('-views')[:5]  # 조회수가 높은 상위 5개 게시글 가져오기
    recent_posts = Post.objects.order_by('-created_at')[:5]  # 최신 게시글 가져오기
    return render(request, 'main.html', {'concern_posts': concern_posts, 'hot_posts': hot_posts, 'recent_posts': recent_posts})



def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'post_detail.html', {'post': post})

    return redirect(f"/detail/{post_id}")

