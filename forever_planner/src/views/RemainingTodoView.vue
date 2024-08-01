<template>
  <div class="w-full h-screen flex flex-col justify-between">
    <div class="w-full h-full bg-[#f5f7fd] p-2 flex flex-col">
      <header class="header">
        <button type="button" @click = "backWards" class="headerBtn"><i class="fa-solid fa-chevron-left w-[20px] h-[20px]" id="backDrawThing"></i></button>
        <button type="button" class = "allCompleteBtn" @click = "allTodoSetComplete"><b>모두 완료</b></button>
      </header>
      <b><p class ="remainingTxt">완료하지 않은 할 일이<br />
        <span class="remainingTodoNum">0</span>개 있습니다.</p></b>


        <RemainingTodoThingDiv />
       <!-- <div class="remainingSettingDiv">
        <div class="batchRemainingTodo">
          <p class="batchP">D+<span class="remainingDate">0</span></p>
          <p class="remainingTodoDate">0월 0일</p>
          <button type="button" class="delayButton">미루기</button>
          <button type="button" class="todoEditBtn" @click="todaysTodoDateClick">
            <p class="todoTag">중요</p>
            <p class="todoTxt">ㅊㄹㄹㄹ</p>
            <button type="button" class ="todoCheck" ><i class="fa-regular fa-square"></i></button>
          </button>
        </div>
      </div>  -->
    </div>
    <FooterVue />
  </div>
</template>
<script>
  import FooterVue from '@/components/FooterVue.vue';
  import { onMounted } from 'vue';
  import { useStore } from '@/stores/store.js';
  import { storeToRefs } from 'pinia';
  import { useRouter } from 'vue-router';
  import RemainingTodoThingDiv from '@/views/remainingTodoThing/RemainingTodoThingDiv.vue'

  export default{
    name: 'RemainingTodo-View',
    components: {
        FooterVue,
        RemainingTodoThingDiv,
    },
    data() {
        return{};
    }, 
    setup(){
      const store = useStore();
      const { isClicked } = storeToRefs(store);
      const router = useRouter(); //useRouter로 Vue Router 주입

      onMounted(() => {
        isClicked.value = 'remainingTodo';
        window.scrollTo(0, 0);
      });

      const backWards = () =>{
        router.push({name: 'home'});
      };

      const allTodoSetComplete = () => { 
        
      }

      return{
        onMounted,
        backWards,
      }
    }
  }
</script>
<style scoped>
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

.header{
  /*position: fixed;*/
  top:0;
  background-color: #f5f7fd;
}
.headerBtn{
  padding:10px;
  width:40px;
  font-size: larger;
  border-radius: 10px;
}
.headerBtn:hover{
  animation-name: touchBtn;
  animation-duration: 0.1s;
  animation-fill-mode: forwards;
}
.allCompleteBtn{
  float:right;
  padding:10px;
  width:max-content;
  margin-right: 5px;
  border-radius: 10px;
  color:#354387
}
.allCompleteBtn:hover{
  animation-name: touchBtn;
  animation-duration: 0.1s;
  animation-fill-mode: forwards;
}

.remainingTxt{
    padding:10px;
    font-size: x-large;
    padding-bottom: 20px;
}
.remainingTodoNum{
    color:deepskyblue;
}

.batchP{
    font-size:medium;
    padding-bottom: 2px;
}
.remainingTodoDate{
    font-size:smaller;
}
.batchRemainingTodo {
  background-color: #FFFFFF;
  position: relative;
  margin: 5px;
  padding: 10px;
  border-radius: 10px;
}
.todoEditBtn {
  width: 100%;
  height:fit-content;
  background-color: #e4d0db;
  border-radius: 8px;
  padding: 15px;
  margin-top: 10px;
  color: #8F9095;
  font-size: small;
  text-align: left;
  position: relative;
}
.todoEditBtn:hover{
  animation-name: touchBtn;
  animation-duration: 0.1s;
  animation-fill-mode: forwards;
}
.todoCheckBox{
    float:right;
}
.todoCheck{
  float:right;
    text-align: center;
    position: absolute;
    padding:10px;
    right:10px;
    top:8px;
    border-radius: 10px;
    margin-right: 5px;
    font-size: large;
}
.todoTxt{
  color: #965d5d;
}
.todoTag{
  font-size: xx-small;
}
.delayButton{
  float:right;
  position: absolute;
  padding: 10px;
  right:10px;
  top:12px;
  color:#64656a;
  border-radius: 10px;
}
.delayButton:hover{
  animation-name: touchBtn;
  animation-duration: 0.1s;
  animation-fill-mode: forwards;
}
</style>