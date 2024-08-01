<template>
  <CategoryModal v-if="categoryModalState" />
  <PostModal v-if="postModalState" />
  <PostCategoryModal v-if="postCategoryModalState" />
  <ConfirmModal v-if="confirmModalState" />

  <div class="h-screen flex flex-col">
    <div class="planetTxtBar">
      <button type="button" @click="planetBtnClick" class="planetTxtBtn">Planet v</button>
      <button type="button" @click="goSettingBtnClick" class="goSettingBtn"><i class="fa-solid fa-gear"></i></button>

      <div class="checkTodoTagModal" tabindex="-1" v-if="isModalVisible" ref="checkTodoTagModal" @blur="closeModal">
        <button
          type="button"
          v-for ="tag in checkTodoTags"
          :key="tag.categoryId"
          class="checkTodoTagBtn" 
          :value="tag.categoryTitle" 
          @click="checkTodoTagClick(tag.categoryTitle)">
          <span :class="['tag1Round'+'tag'+tag.categoryColor+'Round']">●</span>
          {{ tag.categoryTitle }}
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

      <div v-if="settings.setVisibleNotYetTask">
        <button type="button" class="remainingTodoBtn" @click="remainingTodoClick">
          <span><span class="remainingArray">{{ arrayLength_length }}</span>개의 남은 할 일</span><span class="goRight">></span>
        </button>
      </div>

        <div class="todaysTodo" v-if="settings.setVisibleTodayTask">
          <p>오늘</p>
          <p class="todaysTodoDate">0월 0일</p>

          <div>
             <!--임시로 하나 추가-->
            <div class="unCompTodo">
              <p class="date">2024.07.18</p>
              <span class="unCompTodoTxt">아무말</span>
              <button type="button" class ="unCompTodoCheck" ><i class="fa-regular fa-square"></i></button>
            </div>
          </div>

          <button type="button" class="todoEditBtn" @click="handleClickCategoryModal">+ 할 일을 추가하세요</button>
        </div><br />

        <div class="todaysTodo" v-if="settings.setVisibleSomeTask">
          <p>언젠가</p>
          
          <div>
            <!--임시로 하나 추가-->
            <div class="unCompTodo">
              <p class="date">클래스명은같은데들어갈내용이다름</p>
              <span class="unCompTodoTxt">아무말</span>
              <button type="button" class ="unCompTodoCheck" ><i class="fa-regular fa-square"></i></button>
            </div>
          </div>
          
          
          <button type="button" class="todoEditBtn" @click="someDayTodoDateClick">+ 할 일을 추가하세요</button>
        </div>
      </div>
    </div>

    <FooterVue />
  </div>
</template>

<script>
import FooterVue from '@/components/FooterVue.vue';
import {nextTick, onMounted,  watchEffect, ref, computed, getCurrentInstance } from 'vue';
import { storeToRefs } from 'pinia';
import { useStore } from '@/stores/store.js';
import { useRouter } from 'vue-router';
//import DateModal from '@/components/Calendar/DateModal.vue';
import CategoryModal from '@/components/Calendar/Category/CategoryModal.vue';
import PostModal from '@/components/Calendar/Post/PostModal.vue';
import PostCategoryModal from '@/components/Calendar/Category/PostCategoryModal.vue';
import ConfirmModal from '@/components/Calendar/ConfirmModal.vue';
import { useModalStore } from '@/stores/modalStore.js';
//dddd


import axios from 'axios';


export default {
  name: 'Home-View',
  components: {
    FooterVue,
    CategoryModal,
    PostModal,
    PostCategoryModal,
    ConfirmModal,

  },
   data() {
    return {};
  },
  setup() {
    const store = useStore();
    const { isClicked } = storeToRefs(store);
    const isModalVisible = ref(false); 
    const router = useRouter(); //useRouter로 Vue Router 주입
    const { dateModalState, categoryModalState, postModalState, postCategoryModalState, confirmModalState  } = storeToRefs(useModalStore());
    const { handleClickCategoryModal } = useModalStore();
    const checkTodoTags = ref([]);
    const instance = getCurrentInstance(); // 현재 인스턴스 가져오기
    const $isVisibleNotYetTask = instance.appContext.config.globalProperties.$isVisibleNotYetTask;
    const $isVisibleTodayTask = instance.appContext.config.globalProperties.$isVisibleTodayTask;
    const $isVisibleSomeTask = instance.appContext.config.globalProperties.$isVisibleSomeTask;
    const settings = ref({
      setVisibleNotYetTask: Boolean($isVisibleNotYetTask),
      setVisibleTodayTask: Boolean($isVisibleTodayTask),
      setVisibleSomeTask: Boolean($isVisibleSomeTask),
    })
    const arrayLength_length = ref(0);
    


    function handleStopScroll() {
      if (dateModalState.value) {
        document.documentElement.style.overflow = 'hidden';
      } else {
        document.documentElement.style.overflow = 'auto';
      }
    }

    const getCheckTodoModal = async () =>{
      try{
        const res = await axios.get(`http://34.146.205.159:8000/category/all?format=json`);
        checkTodoTags.value = res.data;
        //console.log(`데이터 받아옴 ${JSON.stringify(checkTodoTags.value)}`);
      }catch{
        console.log("데이터 받아오기 실패", error);
      }
    }

    const getRemainingTodoArray = async () => {
      try{
        const res = await axios.get(`http://34.146.205.159:8000/home/all?format=json`);
        arrayLength_length.value = Object.keys(res.data).length;
        //console.log(`데이터 받아옴 ${arrayLength_length.value}`);
      }catch{
        console.log("데이터 받아오기 실패", error);
      }
    }

    onMounted(async() => {
      isClicked.value = 'home';
      window.scrollTo(0, 0);
      await getCheckTodoModal();
      await getRemainingTodoArray();
    });

    watchEffect(() => {
      handleStopScroll();  
      const remainingArrayElement = document.querySelector(".remainingArray");
      if (remainingArrayElement) {
      remainingArrayElement.innerHTML = arrayLength_length.value;
      }
    });

    const planetBtnClick = async() => {
      await nextTick(()=> {
        const modalElement = document.querySelector('.checkTodoTagModal');
        if (modalElement ) {
          modalElement.focus();
        }
      });
      isModalVisible.value = true;
    };


    const checkTodoTagClick = (value) =>{
      console.log(value);
        router.push({ path: '/checkTodo', query: { tag: value } });
    }

    const someDayTodoDateClick = () =>{
      console.log("버튼 눌림");
      //handleClickCategoryModal처럼 동작

    }

    return {
      onMounted,
      handleStopScroll,
      watchEffect,
      planetBtnClick,
      checkTodoTagClick,
      userIconClick() {
        alert("프로필 편집으로 이동하기 위한 버튼");
        // 프로필 편집으로 이동하기 위한 버튼
      },
      remainingTodoClick() {
        router.push('remainingTodo');
      },
      closeModal(){
        setTimeout(()=>isModalVisible.value = false,300);
      },
      todaysTodoDateClick() {

      },
      goSettingBtnClick() {
        router.push({ name: 'setting' });
      },
      isModalVisible,
      handleClickCategoryModal,
      categoryModalState,
      postModalState,
      postCategoryModalState,
      confirmModalState, 

      checkTodoTags,
      someDayTodoDateClick,
      settings,

      getRemainingTodoArray,
      arrayLength_length,
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
  margin-right:10px;
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
  width:98%;
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
  font-size: larger;
  color: #8F9095;
}
.goRight{
  float:right;
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
  margin-left:5px;
}
.checkTodoTagBtn{
  width:100%;
  text-align: start;
  font-size:medium;
  border-width: 0px 0px 1px 0px;
  border-radius:10px;
}
.checkTodoTagBtn:hover{
  animation-name: touchBtn;
  animation-duration: 0.1s;
  animation-fill-mode: forwards;
}
.tag1Round{ 
  color:#5A7CD5;
}
.tag2Round{ 
  color:#5A7CD5;
}
.tag3Round{ 
  color:#5A7CD5;
}


.unCompTodo{
    position: relative;
    border-style: solid;
    border-color: #3d456e;
    border-width:  0px 0px 0px 7px;
    background-color: #8e99ce;
    width:100%;
    border-radius: 5px;
    padding: 10px;
    margin-top:5px;
}
.unCompTodo:hover{
  animation-name: touchBtn;
  animation-duration: 0.1s;
  animation-fill-mode: forwards;
}
.compTodo{
    position: relative;
    background-color: #8e99ce;
    width:100%;
    border-radius: 5px;
    padding: 10px;
    margin-top: 5px;
}
.compTodo:hover{
  animation-name: touchBtn;
  animation-duration: 0.1s;
  animation-fill-mode: forwards;
}


.date{
    font-size: xx-small;
}
.unCompTodoCheck{
    float:right;
    text-align: center;
    position: absolute;
    padding:10px;
    right:0px;
    top:7px;
    border-radius: 10px;
    margin-right: 5px;
}

</style>
