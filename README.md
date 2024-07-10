# Forever

<div align="center">
  <h3>To-Do 리스트와 플래너 기능을 결합한 일정 관리형 어플리케이션</h3>
</div>

## 📋 개요
Firebase와 GitHub 등 다양한 개발 플랫폼을 학습하기 위해 진행된 프로젝트입니다.

이 앱은 사용자의 일정 관리를 위해 로그인을 필요로 하며, 일정 저장 및 캘린더 확인 기능을 제공합니다. Planit과 Todo-mate와 같은 인기 일정 관리 앱을 참고하여 클론 코딩 방식으로 제작되었습니다.

## 🛠 기능별 설계

### 회원 가입 및 로그인
- Firebase Authentication을 사용하여 이메일/비밀번호, Google 계정 등의 방법으로 회원 가입 및 로그인을 구현합니다.

### 캘린더
- 캘린더 뷰를 제공하여 캘린더 내에서 카테고리 선택 및 내용 작성이 가능합니다(커스텀 가능).
- 캘린더에 표시할 항목을 카테고리 별로 확인할 수 있도록 지원합니다.

### 일기 기능
- 어플리케이션 내에서 텍스트와 이미지를 삽입하여 일기를 작성하고, 이를 지정된 범위의 친구와 나눌 수 있습니다.

### 친구 기능
- 아이디, 링크, 카카오톡 초대 기능을 이용하여 친구를 초대할 수 있습니다(카카오톡 API 사용).

### 프로필 편집
- 본인의 이름, 자기 소개, 프로필 사진 수정 기능과 본인의 랜덤 코드(식별 코드), 팔로잉/팔로워 확인 기능이 포함됩니다.

### 테마 커스텀
- 테마 색상 변경 기능을 지원합니다.

### 설정
- 화면 모드(다크, 라이트 모드 지원)
- 홈 화면에 대한 설정(미완료 할 일 등)
- 지난 달 통계 확인(할 일 체크 유무)
- 폰트 설정
- 자주 묻는 질문(FAQ), 문의
- 로그인, 탈퇴, 로그아웃

## ⭐️ 핵심 기술

### 파이어베이스 (Firebase)
- 회원 가입 및 로그인
- 게시글 작성, 저장 및 편집

### 카카오톡 API (KakaoTalk API)
- 카카오톡 API을 이용한 회원 가입
- 친구 초대(링크 공유)

### 안드로이드 스튜디오 (Android Studio)와 GitHub
- 어플리케이션을 개발하기 위해 안드로이드 스튜디오와 GitHub을 활용합니다.
