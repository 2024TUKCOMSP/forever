<template>
<div class="bg-[#f5f7fd] justify-between">
  <header class="settingHeader">
    <button type="button" @click = "backWards" class="settingHeaderBtn">&lt;</button>
  </header>
  <br />
  <div class= "settingScreen">
    <b><h1>설정</h1></b>

    <button type="button" class="defaultBtn">카테고리 편집 <span class="goRight">&gt;</span></button>

    <br /><br />

    <p class="settingP">화면 모드</p>
    <div class="settingModeCss">
      <button type="button" class="screenMode" @click="isClickScreenModeBtn('Light')">라이트 모드 <span class="isChecked" id ="lightModeTxt"></span></button>
      <button type="button" class="screenMode" @click="isClickScreenModeBtn('Dark')">다크 모드<span class ="isChecked" id="darkModeTxt"></span></button>
    </div> <br />

    <p class ="settingP">홈 화면 설정</p>
    <div class="settingModeCss">
      <p>미완료 할 일</p>
      <p>오늘</p>
      <p>언젠가</p>
    </div><br />

    <p class="settingP">캘린더 설정</p>
    <button type="button" class="defaultBtn">캘린더에 표시할 항목</button> <br />

    <button type="button" class ="defaultBtn">지난 달 통계 확인하기<span class="goRight">&gt;</span></button><br /><br /><br />

    <button type="button" class ="defaultBtn2">로그아웃</button><br /><br /><br />
    <button type="button" class ="defaultBtn2">탈퇴</button><br />
  </div>
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

    var isClickScreenModeBtn = function(txt){
        if(txt == 'Dark'){
          //다크 모드 동작
          document.getElementById("test").innerHTML = "변경된 span값";
          document.getElementById("test").innerHTML = "변경된 span값";
        }else{
          //라이트 모드 동작
          document.getElementById("test").innerHTML = "변경된 span값";
          document.getElementById("test").innerHTML = "변경된 span값";
        }
      }
    return{
      backWards,
      isClickScreenModeBtn,
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
    transform:scale(0.97);
    background-color: #ECEDF2;
    align-self: center;
  }
} 

.settingHeader{
  position: fixed;
  top:0;
  background-color: #f5f7fd;
}
.settingHeaderBtn{
  font-size:xx-large;
}
.settingScreen{
  background-color: #f5f7fd;
  width:auto;
  height: 100vh;
  align-self: center;
  text-align: center;
  margin-top: 20px;
}
.goRight{
  float:right;
}
.settingP{
  font-size: small;
  margin:0px 0px 0px 15px;
  display: flex;
  justify-self:start;
}
.settingSpan{
  margin: 0px 0px 0px 5px;
}
h1{
  font-size:xx-large;
  padding-bottom: 5px;
  text-align: start;
  padding-left: 10px;
}
.defaultBtn{
  background-color: #fff;
  border-radius: 10px;
  margin:5px;
  padding:10px;
  width:95%;
  text-align: start;
}
.defaultBtn2{
  background-color: #fff;
  border-radius: 10px;
  margin:5px;
  padding:10px;
  width:95%;
  text-align: start;
  color:red;
}
.settingModeCss{
  width: 95%;
  border-radius: 10px;
  background-color: #fff;
  margin-left: 10px;
  margin-right: 10px;
  text-align: left;
  padding-left: 10px;
  margin-top: 5px;
}
.screenMode{
  background-color: #fff;
  padding:5px;
  padding-right: 10px;
  width:100%;
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
label{
  border-width: 0px 0px 1px 0px;
  width: 98%
}
.radioBtn{
  float:right;
}
label:hover{
  animation-name: touchBtn;
  animation-duration: 0.1s;
  animation-fill-mode: forwards;
}
</style>