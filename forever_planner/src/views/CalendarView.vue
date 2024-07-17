<template>
  <div class="w-full h-screen flex flex-col justify-between">
    <div class="w-full h-full bg-[#f5f7fd] p-2 flex flex-col justify-end">
      <div class="text-2xl font-semibold p-3">7월</div>
      <CalendarVue class="w-full h-full"/>
    </div>
    <FooterVue />
  </div>
</template>

<script setup>
import CalendarVue from '@/components/Calendar/CalendarVue.vue'
import FooterVue from '@/components/FooterVue.vue';
import { storeToRefs } from 'pinia';
import { useStore } from '@/stores/store.js';
import { onMounted } from 'vue';

const { isClicked } = storeToRefs(useStore());

onMounted(() => {
  isClicked.value = 'diary'
})
</script>

<style scoped>
</style>