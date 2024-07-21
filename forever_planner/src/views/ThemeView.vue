<template>
     <div class="w-full h-screen flex flex-col justify-between">
    <div class="w-full h-full bg-[#f5f7fd] p-2 flex flex-col">
      dddd
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
</style>