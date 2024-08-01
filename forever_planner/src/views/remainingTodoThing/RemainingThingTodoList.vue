<template>
  <div class="remainingSettingDiv">
   <!-- <div v-if="remainingTodos.length > 0">-->
    <div v-for="(todo, index) in remainingTodos" :key="index" class="batchRemainingTodo"  >
    <div v-if = "!todo.post.isFinished.value" class="todoItem"> 
      <b><p class="batchP">D<span class="remainingDate">{{ fixDaycount(todo.daycount) }}</span></p></b>
        <p class="remainingTodoDate">7월 {{ todo.calendarDate }}일</p>
        <button type="button" class="todoEditBtn" @click="todaysTodoDateClick" :style="borderColor(todo.post.category.categoryColor)">
          <p class="todoTag">{{ todo.post.category.categoryTitle }}</p>
          <p class="todoTxt">{{ todo.post.title }}</p>
          <button type="button" class ="todoCheck"  @click="changeFinishedState(todo.post.isFinished, todo.post.postId)" >
            <i class="fa-regular fa-square"></i>
          </button>
          </button>
          <div>
        </div>
        </div>
    </div>
</div>
</template>


<script setup>
import { onMounted, ref } from 'vue';
import { useStore } from '@/stores/store';
import { storeToRefs } from 'pinia';

const store = useStore();
const { colors } = storeToRefs(store);
const { getColors } = store;
const { changeFinishedState } = store;

const usingTheme = ref(null);

const props = defineProps({
    remainingTodos: {
        type: Array,
        default: () => []
    }
})

const fixDaycount = (daycount) => {
  return daycount.replace(/\+\-/g, '-');
}

const backgroundColor = (backgroundColor) => {
 // console.log(backgroundColor);
  //console.log(usingTheme.value);
 // if (usingTheme.value == null) return { backgroundColor: '#ffffff' };
  return { backgroundColor: usingTheme.value.colorList[backgroundColor].colorCode};
}

onMounted(async() => {
  await getColors();
  usingTheme.value = colors.value.find(theme => theme.is_use);
});

const todaysTodoDateClick = () => {
    console.log("Todo clicked");
}

const borderColor = (categoryColor) => {
  return { borderColor: usingTheme.value.colorList[categoryColor].colorCode, 
      backgroundColor: `${usingTheme.value.colorList[categoryColor].colorCode}44`
   }; // 서버에서 받은 categoryColor를 사용하여 border-color 설정
};

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
    color:#b10808;
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
  color: #161619;
  font-size: small;
  text-align: left;
  position: relative;
  border-color: #452927;
  border-width:  0px 0px 0px 7px;
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
  color: #241111;
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