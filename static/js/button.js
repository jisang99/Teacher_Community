


const iconButton = document.getElementById('like_Btn');
const icon = document.getElementById('heart_icon');
let isRed = false;

iconButton.addEventListener('click', () => {
    if (isRed) {
        // 아이콘 색을 원래 색상으로 변경
        icon.style.color = '#ff0000';
        isRed = false;
    } else {
        // 아이콘 색을 빨간색으로 변경
        icon.style.color = '#ff0000';
        isRed = true;
    }
});
