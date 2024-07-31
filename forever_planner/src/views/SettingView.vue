<template>
<div class="bg-[#f5f7fd] justify-between">
  <header class="settingHeader">
    <div class="settingHeaderDiv">
    <button type="button" @click = "backWards" class="settingHeaderBtn"> <i class="fa-solid fa-chevron-left w-[20px] h-[20px]" id="backDrawThing"></i> </button>
  </div>
  </header>
  <br />
  <div class= "settingScreen" @click = "closeEditCategoryModal">
    <CategoryModal v-if ="editModeState == true" ref="categoryModal" />
    <b><h1> 설정</h1></b>

    <button type="button" class="defaultBtn" @click="editCategoryBtnClick">카테고리 편집 <span class="goRight">&gt;</span></button>

    <br /><br />

    <p class="settingP">화면 모드</p>
    <div class="settingModeCss">
      <button type="button" class="screenMode" @click="isClickScreenModeBtn('Light')">라이트 모드 <span class="isChecked" id ="lightModeTxt"><i class="fa-solid fa-check"></i></span></button>
      <button type="button" class="screenMode" @click="isClickScreenModeBtn('Dark')">다크 모드<span class ="isChecked" id="darkModeTxt"></span></button>
      <button type="button" class="screenMode" @click="isClickScreenModeBtn('Auto')">시스템(자동)<span class ="isChecked" id="autoModeTxt"></span></button>
    </div> <br />

    <p class ="settingP">홈 화면 설정</p>
    <div class="settingModeCss">
      <p class ="settingModeP">미완료 할 일<input role ="switch" type="checkbox" class="settingModeToggle" v-model ="settings.isVisibleNotYetTask" /></p>
      <p class ="settingModeP">오늘<input role ="switch" type="checkbox" class="settingModeToggle" v-model="settings.isVisibleTodayTask" /></p>
      <p class ="settingModeP">언젠가<input role ="switch" type="checkbox" class="settingModeToggle" v-model ="settings.isVisibleSomeTask" /></p>
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
import { onMounted, ref, watch, onUnmounted, nextTick } from 'vue';
import axios from 'axios'; 
import CategoryModal from '@/components/Calendar/Category/CategoryModal.vue';

export default {
  name: 'Setting-View',
  components : {
    CategoryModal,
  },
  data() {
    return {};
  },
  setup() {
    const router = useRouter(); 
    const editModeState = ref(false);
    const settings = ref({
      isVisibleNotYetTask: true,
      isVisibleTodayTask: true,
      isVisibleSomeTask: true,
    })

    const updateSettings = async (key, value) => {
      try {
        const response = await axios.put(`http://34.146.205.159:8000/Setting/home`, settings.value);
        console.log("설정 업데이트", response.data);
      }catch(error){
        console.log("업테이트 중 오류 발생", error);
      }
    }

    const backWards = () =>{
      router.push({name: 'home'});
    }

    onMounted(()=>{
      window.scrollTo(0, 0);
    })

    //setting Object가 변경되었을 때에 설정 업데이트. 
    watch(settings, (newSettings)=> {
      updateSettings();
    }, { deep: true });

    var isClickScreenModeBtn = (txt) => {
        if(txt == 'Dark'){
          //다크 모드 동작
          document.getElementById("darkModeTxt").innerHTML="<i class=\"fa-solid fa-check\"></i>";
          document.getElementById("lightModeTxt").innerHTML="";
          document.getElementById("autoModeTxt").innerHTML="";
          alert("구현중..");
        }else if(txt == 'Light'){
          //라이트 모드 동작
          document.getElementById("lightModeTxt").innerHTML="<i class=\"fa-solid fa-check\"></i>";
          document.getElementById("darkModeTxt").innerHTML="";
          document.getElementById("autoModeTxt").innerHTML="";
        }else{
          document.getElementById("lightModeTxt").innerHTML="";
          document.getElementById("darkModeTxt").innerHTML="";
          document.getElementById("autoModeTxt").innerHTML="<i class=\"fa-solid fa-check\"></i>";
        }
      }

      const editCategoryBtnClick = () =>{
        setTimeout(()=>{
          editModeState.value = !editModeState.value;
          console.log("카테고리 편집 버튼 클릭"+editModeState.value);
        },10);
      };

      const closeEditCategoryModal = () =>{
        if(editModeState.value == true){
          editModeState.value = false;
        }
      }

    return{
      backWards,
      isClickScreenModeBtn,
      onMounted,
      updateSettings,
      settings,
      editCategoryBtnClick,
      editModeState,
      closeEditCategoryModal,
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

#backDrawThing{
  margin:10px;
}
.settingHeader{
  position: fixed;
  top:0;
  background-color: #f5f7fd;
  width: 31em;
}
.settingHeaderDiv{
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
.settingModeP{
  padding:5px;
  border-width: 0px 0px 1px 0px;
  width:98%;
  position: relative;
}
[type="checkbox"] {
  appearance: none;
  position: relative;
  border: max(2px, 0.1em) solid gray;
  border-radius: 1.25em;
  width: 2.25em;
  height: 1.25em;
}
[type="checkbox"]::before {
  content: "";
  position: absolute;
  left: 0;
  width: 1em;
  height: 1em;
  border-radius: 50%;
  transform: scale(0.8);
  background-color: gray;
  transition: left 250ms linear;
}
[type="checkbox"]:checked::before {
  background-color: #ffffff;
  left: 1em;
}
[type="checkbox"]:checked {
  background-color: rgb(46, 91, 255);
  border-color: rgb(46, 91, 255);
}
.settingModeToggle{
  cursor:pointer;
  float: right;
  position: absolute;
  right:10px;
  top:7px;
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