<template>
  <header class="settingHeader">
    <button type="button" @click = "backWards" class="settingHeaderBtn">뒤로가기</button>
  </header>
  <br />
  <div class= "settingScreen">
    <b><h1 class = "h1">설정</h1></b>

    <button type="button" class="defaultBtn">카테고리 편집 >> </button>

    <br /><br />

    <p class="settingP">화면 모드</p>
    <div class="settingModeCss">
      <button type="button" class="screenMode">라이트 모드 <span class="isChecked"></span></button>
      <button type="button" class="screenMode">다크 모드<span class ="isChecked"></span></button>
    </div> <br />

    <p class="settingP">캘린더 설정</p>
    <button type="button" class="defaultBtn">캘린더에 표시할 항목</button> <br />

    <button type="button" class ="defaultBtn">지난 달 통계 확인하기</button><br /><br /><br />

    <button type="button" class ="defaultBtn2">로그아웃</button><br /><br /><br />
    <button type="button" class ="defaultBtn2">탈퇴</button><br />
  </div>
</template>

<script>
import {useRouter} from 'vue-router';

export default {
  name: 'Setting-View',
  data() {
    return {};
  },
  setup() {
    const router = useRouter(); 

    const backWards = () =>{
      router.push({name: 'home'});
    }
    return{
      backWards,
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
  width:74vh; /*임시 처리*/
}
.settingScreen{
  background-color: #f5f7fd;
  width:auto;
  height: 100vh;
}
.settingP{
  font-size: small;
  margin:0px 0px 0px 10px;
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
  padding-left: 20px;
  width:95%;
  text-align: start;
}
.defaultBtn2{
  background-color: #fff;
  border-radius: 10px;
  margin:10px;
  padding:5px;
  padding-left: 20px;
  width:95%;
  text-align: start;
  color:red;
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
  border-width: 0px 0px 1px 0px;
  border-radius: 10px;
  text-align: start;
}
.isChecked{
  float: right;
}
button:hover{
  animation-name: touchBtn;
  animation-duration: 0.1s;
  animation-fill-mode: forwards;
}
</style>