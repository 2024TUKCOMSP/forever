<template>
     <div class="w-full h-screen flex flex-col justify-between">
    <div class="w-full h-full bg-[#f5f7fd] p-2 flex flex-col">
      <header>
      <div class="planetBannerCSS">Colors</div> <br />
    </header>
    <div class="colorPalette">
      <button type="button" id="defaultColor" class="batchColorBtn">
        <span id ="defaultColor" class ="batchSpan">Planit 3.0</span> <span class="goRight" id="defaultColor">적용중</span>

      </button>
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
.batchColorBtn{
  background-color: #fff;
  padding: 10px;
  width:100%;
  border-radius: 10px;

}
</style>