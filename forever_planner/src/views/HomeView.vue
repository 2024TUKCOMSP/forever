<template>
  <div class="h-screen flex flex-col">
    <div class="planetTxtBar">
      <button type="button" @click="planetBtnClick()" class="planetTxtBtn">Planet v</button>
      <button type="button" @click="goSettingBtnClick()" class="goSettingBtn">설정</button>
    </div>
    <div class="flex-grow w-full bg-[#f1f5f8] p-2 flex flex-col">
      <div class="userBar">
        <div class="userIcon">
          <button type="button" @click="userIconClick()" class="userIconBtn">클릭</button>
          <p class="userName">디폴트이름</p>
        </div>
      </div>
      <button type="button" class="remainingTodoBtn" @click="remainingTodoClick()">
        <span>2개의 남은 할 일</span>
        <span class="remainingTodoTxt">&gt;</span>
      </button>
      <div class="todaysTodo">
        <p>오늘</p>
        <p class="todaysTodoDate">0월 0일</p>
        <button type="button" class="todoEditBtn" @click="todaysTodoDateClick()">+ 할 일을 추가하세요</button>
      </div>
    </div>
    <FooterVue />
  </div>
</template>

<script>
import { useRouter } from 'vue-router';
import FooterVue from '@/components/FooterVue.vue'; // FooterVue 컴포넌트 등록

export default {
  name: 'HomeView',
  components: {
    FooterVue,
  },
  setup() {
    const router = useRouter();
    return {
      router,
    };
  },
  methods: {
    userIconClick() {
      alert("dkdkkd");
      // 프로필 편집으로 이동하기 위한 버튼
    },
    remainingTodoClick() {
      alert("");
    },
    planetBtnClick() {

    },
    todaysTodoDateClick() {

    },
    goSettingBtnClick() {
      this.router.push({ path: '/setting' });
    },
  },
}
</script>

<style scoped>
.planetTxtBar {
  padding-left: 10px;
  background-color: #F1F5F8;
  position: relative;
  font-size: larger;
  color: #8F9095;
}
.planetTxtBtn {
  padding-left: 10px;
  padding-right: 10px;
  padding-top: 10px;
}
.planetTxtBtn:hover {

}
.background {
  background-color: #F1F5F8;
}
.goSettingBtn {
  font-size: medium;
  position: absolute;
  top: 0;
  right: 0;
  padding: 10px;
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
  background-color: #FFFFFF;
  position: relative;
  margin: 5px;
  padding: 10px;
  border-radius: 10px;
  color: #5A7CD5;
  font-size: small;
  text-align: left;
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
  background-color: #ECEDF2;
  border-radius: 8px;
  padding: 15px;
  margin-top: 10px;
  color: #8F9095;
  font-size: small;
  text-align: left;
}
</style>
