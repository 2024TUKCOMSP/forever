<template>
<div class="w-full h-screen flex flex-col justify-between">
  <div class="w-full h-full bg-[#f5f7fd] p-2 flex flex-col">
    <header class="settingHeader">
      <button type="button" @click = "backWards" class="settingHeaderBtn"> <i class="fa-solid fa-chevron-left w-[20px] h-[20px]" id="backDrawThing"></i> </button>
    </header><br />

    <b><h1 class="checkTodoTagName">{{ tag }}</h1></b><br />
    
    <div class="settingModeCss">
      
      <p class="checkTodoP"><b>미완료</b></p>
      <div class="unCompleteTodoDiv">

        <!--임시로 하나 추가-->
        <div class="unCompTodo">
            <p class="date">2024.07.18</p>
            <span class="unCompTodoTxt">아무말</span>
            <button type="button" class ="unCompTodoCheck" ><i class="fa-regular fa-square"></i></button>
        </div>
      
    </div>
    </div><br />

    <div class="settingModeCss">
      <p class="checkTodoP"><b>완료</b></p>
      <div class="completeTodoDiv">

         <!--임시로 하나 추가-->
         <div class="compTodo">
            <div class="bg-[#e4eefc] w-full rounded text-2xs flex h-full"></div>
            <p class="date">2024.07.18</p>
            <span class="compTodoTxt">아무말</span>
            <button type="button" class ="unCompTodoCheck"><i class="fa-solid fa-check"></i></button>
        </div>

      </div>
    </div>
  </div>
  <FooterVue />
</div>
</template>


<script>
import { useRouter, useRoute } from 'vue-router';
import FooterVue from '@/components/FooterVue.vue';

export default{
    name: 'Check-Todo-View',
    components: {
    FooterVue,
  },
    setup() {
      const route = useRoute();
      const tag = route.query.tag;
        const router = useRouter();
        const backWards = () =>{
            router.go(-1);
        }

        return{
            backWards,
            tag,
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
}
.settingHeaderBtn{
  font-size:xx-large;
}
button:hover{
  animation-name: touchBtn;
  animation-duration: 0.1s;
  animation-fill-mode: forwards;
}
.settingScreen{
  background-color: #f5f7fd;
  width:auto;
  height: 100vh;
  align-self: center;
  text-align: center;
  margin-top: 20px;
}
.checkTodoTagName{
  color:#3d456e;
}
.checkTodoP{
    padding:10px;
}
h1{
  font-size:xx-large;
  padding-top: 10px;
  padding-bottom: 5px;
  text-align: start;
  padding-left: 10px;
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

.unCompTodo{
    position: relative;
    border-style: solid;
    border-color: #3d456e;
    border-width:  0px 0px 0px 7px;
    background-color: #8e99ce;
    width:94%;
    margin: 0px 10px 10px 10px;
    border-radius: 5px;
    padding: 10px;
}
.unCompTodo:hover{
  animation-name: touchBtn;
  animation-duration: 0.1s;
  animation-fill-mode: forwards;
}
.compTodo{
    position: relative;
    background-color: #8e99ce;
    width:94%;
    margin: 0px 10px 10px 10px;
    border-radius: 5px;
    padding: 10px;
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