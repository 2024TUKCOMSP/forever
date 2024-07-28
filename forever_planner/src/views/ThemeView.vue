<template>
  <div class="w-full h-screen flex flex-col justify-between">
    <div class="w-full h-full bg-[#f5f7fd] p-4 flex flex-col">
      <div class="text-xl font-semibold py-4">Colors</div>
      <div class="flex gap-4 flex-col">
        <div v-for="theme in colors" :key="theme">
          <ThemeVue 
            :theme="theme" />
        </div>
      </div>
    </div>
    <FooterVue />
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue';
import axios from 'axios';
import FooterVue from '@/components/FooterVue.vue';
import ThemeVue from '@/components/Theme/ThemeVue.vue';

const isSelected = ref([false, true]);
const colors = ref([]);

const getColors = async () => {
  const res = await axios.get(`http://34.146.205.159:8000/theme/all/?format=json`);
  colors.value = res.data;
};

onMounted(async() => {
  await getColors();
  console.log(colors.value);
});
</script>

<style scoped>
</style>