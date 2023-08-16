document.addEventListener('DOMContentLoaded', function() {
    const loginButton = document.getElementById('btn');
    const errorMessage = document.getElementById('error-message');
  
    errorMessage.style.display = 'none'; // 페이지 로드 시에는 문구 숨김 처리
  
    loginButton.addEventListener('click', async (event) => {
      event.preventDefault(); // 기본 동작(페이지 새로고침)을 막음
  
      const response = await fetch('/login', {
        method: 'POST',
        body: JSON.stringify({
          username: 'yourUsername',
          password: 'yourPassword'
        }),
        headers: {
          'Content-Type': 'application/json'
        }
      });
  
      const data = await response.json();
  
      if (response.ok) {
        // 로그인 성공 처리
        errorMessage.style.display = 'none'; // 성공 시 문구 숨김
      } else {
        // 로그인 실패 처리
        errorMessage.style.display = 'block'; // 실패 시 문구 표시
      }
    });
  });
  