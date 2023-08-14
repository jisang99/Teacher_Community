const likeBtn = document.getElementById("like_Btn");
const postLikesCount = document.getElementById("like_count");
const userLikeCount = document.getElementById("user_like_count");
const postId = '{{ post.id }}';  // 포스트의 ID를 가져옵니다.

likeBtn.addEventListener("click", () => {
    fetch(`/like/${postId}/`)
        .then(response => response.json())
        .then(data => {
            postLikesCount.innerText = data.post_likes_count;
            userLikeCount.innerText = data.user_like_count;

            // 사용자가 좋아요를 누른 경우 버튼 색 변경
            if (data.user_liked) {
                likeBtn.style.color = 'red';
            } else {
                likeBtn.style.color = 'black';  // 사용자가 좋아요를 취소한 경우 버튼 색 원래대로
            }
    });
});