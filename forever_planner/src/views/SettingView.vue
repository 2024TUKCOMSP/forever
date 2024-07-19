<template>
  <header class="settingHeader">
    <button type="button">뒤로가기</button>
  </header>
  <br />
  <div class= "settingScreen">
    <b><h1 class = "h1">설정</h1></b>

    <button type="button">카테고리 편집 >> </button>

    <br /><br />

    <p class="settingP">화면 모드</p>
    <div class="settingModeCss">
      <button type="button" class="screenMode">라이트 모드 <span></span></button>
      <button type="button" class="screenMode">다크 모드<span></span></button>
    </div>

    <p class="settingP">캘린더 설정</p>
      <button type="button" class="defaultBtn">캘린더에 표시할 항목</button>

    <button type="button" class ="defaultBtn">지난 달 통계 확인하기</button>

  </div>
</template>

<script>


export default {
  name: 'Setting-View',
  data() {
    return {};
  },
  setup() {
    

    return{

    }
  }
}
</script>

<style scoped>
/* 애니메이션 */
@keyframes touchBtn{
  0% {
    transform:scale(1);
    background-color: #f5f7fd;
  }

  100% {
    transform:scale(0.95);
    background-color: #ECEDF2;
    align-self: center;
  }
} 

.settingHeader{
  position: fixed;
  top:0;
  background-color: #f5f7fd;
}
.settingScreen{
  background-color: #f5f7fd;
  width:auto;
  height: 100vh;
}
.settingP{
  font-size: small;
}
.h1{
  font-size:xx-large;
  padding-bottom: 5px;
}

.defaultBtn{
  background-color: #fff;
  border-radius: 10px;
  margin:10px;
  padding:5px;
  width:95%;
}
.settingModeCss{
  border-radius: 10px;
  background-color: #fff;
  margin-left: 10px;
  margin-right: 10px;
}
.screenMode{
  background-color: #fff;
  margin-left: 10px;
  margin-right: 10px;
  padding:5px;
  width:95%;
}
</style>