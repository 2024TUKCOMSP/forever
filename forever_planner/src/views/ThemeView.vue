<template>
  <div class="w-full h-screen flex flex-col justify-between">
    <div class="w-full h-full bg-[#f5f7fd] p-4 flex flex-col">
      <div class="text-xl font-semibold py-4">Colors</div>
      <div class="flex gap-4 flex-col">
        <div v-for="theme in isSelected" :key="theme">
          <ThemeVue :isSelected="theme" />
        </div>
      </div>
    </div>
    <FooterVue />
  </div>
</template>

<script setup>
import { ref } from 'vue';
import FooterVue from '@/components/FooterVue.vue';
import ThemeVue from '@/components/Theme/ThemeVue.vue';

const isSelected = ref([false, true]);
</script>

<style scoped>
</style>