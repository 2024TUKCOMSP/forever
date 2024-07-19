<template>
  <!--홈 화면-->

  <div class="h-screen flex flex-col">
    <div class="planetTxtBar">
      <button type="button" @click="planetBtnClick" class="planetTxtBtn">Planet v</button>
      <button type="button" @click="goSettingBtnClick" class="goSettingBtn">설정</button>

          <!--모달 팝업-->
      <div class="checkTodoTagModal" v-show="isModalVisible" >
        <button type="button" class="checkTodoTagBtn">
          <!--컬러 추가-->
          태그명1
        </button><br />
        <button type="button" class="checkTodoTagBtn">
          <!--컬러 추가-->
          태그명2
        </button><br />
        <button type="button" class="checkTodoTagBtn">
          <!--컬러 추가-->
          태그명3
        </button><br />
      </div>
    </div>

    <div class="flex-grow w-full bg-[#f5f7fd] p-2">
      <div class="w-full flex flex-col">
        <div class="userBar">
          <div class="userIcon">
            <button type="button" @click="userIconClick" class="userIconBtn">클릭</button>
            <p class="userName">디폴트이름</p>
          </div>
        </div>
        <button type="button" class="remainingTodoBtn" @click="remainingTodoClick">
          <span>2개의 남은 할 일</span>
          <span class="remainingTodoTxt">&gt;</span>
        </button>
        <div class="todaysTodo">
          <p>오늘</p>
          <p class="todaysTodoDate">0월 0일</p>
          <button type="button" class="todoEditBtn" @click="todaysTodoDateClick">+ 할 일을 추가하세요</button>
        </div>
      </div>
    </div>

  <FooterVue />
  </div>

  
</template>

<script>
import FooterVue from '@/components/FooterVue.vue';
import {onMounted, ref} from 'vue';
import { storeToRefs } from 'pinia';
import { useStore } from '@/stores/store.js';
import { useRouter } from 'vue-router';


export default {
  name: 'Home-View',
  components: {
    FooterVue,
  },
   data() {
    return {};
  },
  setup() {
    const store = useStore();
    const { isClicked } = storeToRefs(store);
    const isModalVisible = ref(false); 
    const router = useRouter(); //useRouter로 Vue Router 주입
    
    onMounted(() => {
    isClicked.value = 'home';
    });

    return {
      isModalVisible,
      onMounted,
      checkTodoTagClick(){
      },
      userIconClick() {
        alert("dkdkkd");
        // 프로필 편집으로 이동하기 위한 버튼
      },
      remainingTodoClick() {
        alert("");
      },
      planetBtnClick() {
        isModalVisible.value = !isModalVisible.value // Toggle modal visibility
      },
      todaysTodoDateClick() {
      },
      goSettingBtnClick() {
        router.push({ name: 'setting' });
      },
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

.flex-grow {
  background-color: #f5f7fd; /* 페이지 내용 배경 색상 */
}

.planetTxtBar {
  padding-left: 10px;
  padding-top: 10px;
  background-color: #f5f7fd;
  position: relative;
  font-size: larger;
  color: #8F9095;
}
.planetTxtBtn {
  padding: 5px;
  padding-left: 10px;
  padding-right: 10px;
  border-radius: 10px;
}
.planetTxtBtn:hover {
  animation-name: touchBtn;
  animation-duration: 0.1s;
  animation-fill-mode: forwards;
}
.background {
  background-color: #f5f7fd;
}
.goSettingBtn {
  font-size: medium;
  position: absolute;
  top: 0;
  right: 0;
  padding: 10px;
  border-radius: 30px;
}
.goSettingBtn:hover{
  animation-name: touchBtn;
  animation-duration: 0.1s;
  animation-fill-mode: forwards;
}
.on{
  display:block;
}

.userIconBtn {
  height: 50px;
  width: 50px;
  background-color: #FFFFFF;
  border-radius: 50%;
  border-color: #FFFFFF;
  margin-bottom: 3px;
}
.userName {
  font-size: x-small;
}
.userBar {
  align-items: start;
  padding: 10px;
}

.remainingTodoBtn {
  width:100%;
  height:auto;
  background-color: #FFFFFF;
  position: relative;
  margin: 5px;
  padding: 10px;
  margin-top: 20px;
  border-radius: 10px;
  color: #5A7CD5;
  font-size: small;
  text-align: left;
}
.remainingTodoBtn:hover{
  animation-name: touchBtn;
  animation-duration: 0.1s;
  animation-fill-mode: forwards;
}
.remainingTodoTxt {
  position: absolute;
  right: 0;
  top: 0;
  padding: 6px 12px 6px 6px;
  font-size: larger;
  color: #8F9095;
}

.todaysTodo {
  background-color: #FFFFFF;
  position: relative;
  margin: 5px;
  padding: 10px;
  border-radius: 10px;
}
.todaysTodoDate {
  font-size: x-small;
  color: #8F9095;
}
.todoEditBtn {
  width: 100%;
  height:fit-content;
  background-color: #f5f7fd;
  border-radius: 8px;
  padding: 15px;
  margin-top: 10px;
  color: #8F9095;
  font-size: small;
  text-align: left;
}
.todoEditBtn:hover{
  animation-name: touchBtn;
  animation-duration: 0.1s;
  animation-fill-mode: forwards;
}


.checkTodoTagModal{
  position:absolute;
  background-color: #FFFFFF;
  width: 150px;
  height:fit-content;
  align-items: start;
  box-shadow: 0px 0px 30px  #8F9095;
  border-radius: 10px;
  padding:10px;
}
.checkTodoTagBtn{
  width:100%;
  text-align: start;
  font-size:medium;
  border-width: 0px 0px 1px 0px;
}
</style>
