<template>
<button type="button" class="todoEditBtn" @click="todaysTodoDateClick">
            <p class="todoTag">중요</p>
            <p class="todoTxt">ㅊㄹㄹㄹ</p>
            <button type="button" class ="todoCheck" ><i class="fa-regular fa-square"></i></button>
          </button>
</template>


<script>

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
</style>