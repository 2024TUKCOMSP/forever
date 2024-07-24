<template>
     <div class="w-full h-screen flex flex-col justify-between">
    <div class="w-full h-full bg-[#f5f7fd] p-2 flex flex-col">
      <header>
      <div class="planetBannerCSS">Colors</div> <br />
    </header>
      <div class="colorPalette">
          
        <div class="form_radio_btn"><label for="defaultColor" class="batchColorRadio">
          Planit 3.0
        <input type="radio" id = "defaultColor" name="colorPalette" value="defaultColor" checked />
        <span></span>
        </label></div>

        <div class="form_radio_btn"><label for="byebyeMyBlueColor" class="batchColorRadio">
          Bye bye My Color
        <input type="radio" id = "byebyeMyBlueColor" name="colorPalette" value="byebyeMyBlueColor" />
        <span></span>
        </label></div>

        <div class="form_radio_btn"><label for="timeAndFallenColor" class="batchColorRadio">
          시간과 낙엽
        <input type="radio" id = "timeAndFallenColor" name="colorPalette" value="timeAndFallenColor" />
        <span></span>
        </label></div>
      </div>
    </div>
    <FooterVue />
  </div>
</template>

<script>
import FooterVue from '@/components/FooterVue.vue';
import {onMounted} from 'vue';
import { storeToRefs } from 'pinia';
import { useStore } from '@/stores/store.js';

export default{
    name: 'Theme-View',
  components: {
    FooterVue,
  },
   data() {
    return {};
  },
  setup() {
    const store = useStore();
    const { isClicked } = storeToRefs(store);
    
    
    onMounted(() => {
    isClicked.value = 'theme';
    });
    return{

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

.planetBannerCSS{
  padding:5px;
  padding-left: 10px;
  padding-top: 10px;
  font-size: larger;
  color:#8F9095;
}
.goRight{
  float:right;
  padding-right: 10px;
}
.batchSpan{
  float:left;
}
.colorPalette{
  width:100%;
}
.batchColorRadio{
  background-color: #fff;
  padding: 10px;
  width: 100%;
  border-radius: 10px;
  margin-bottom: 20px;
  display:inline-block;

}
.batchColorRadio:hover{
  animation-name: touchBtn;
  animation-duration: 0.1s;
  animation-fill-mode: forwards;
}
[type="radio"],
span {
  vertical-align: middle;
  float:right;
}
[type="radio"]{
  vertical-align: middle;
  /*appearance: none*/
}

</style>