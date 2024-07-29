<template>
  <div class="remainingSettingDiv">
      <div class="batchRemainingTodo">
          <p class="batchP">D+<span class="remainingDate">0</span></p>
          <p class="remainingTodoDate">0월 0일</p>
          <button type="button" class="delayButton">미루기</button>
          <!--<button type="button" class="todoEditBtn" @click="todaysTodoDateClick">
            <p class="todoTag">중요</p>
            <p class="todoTxt">ㅊㄹㄹㄹ</p>
            <button type="button" class ="todoCheck" ><i class="fa-regular fa-square"></i></button>
          </button>-->
          <RemainingTodoList />
    </div>
  </div> 
</template>

<script>
import RemainingTodoList from '@/views/remainingTodoThing/RemainingThingTodoList.vue'
import { onMounted, ref } from 'vue';
import axios from 'axios';

export default{
    components: {
        RemainingTodoList
    },
    data() {
        return {};
    },
    setup(){
        const getRemainingTodo = async() =>{
            const res = await axios.get(`http://34.146.205.159:8000/home/all`);
            
        }

        onMounted(async() => {
            await getRemainingTodo();
            console.log("task 받아옴");
        })

        return{

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