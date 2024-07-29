<template>
  <div class="w-full h-screen flex flex-col justify-between">
    <div class="w-full h-full bg-[#f5f7fd] p-4 flex flex-col">
      <div class="text-xl font-semibold py-4">Colors</div>
      <div class="flex gap-4 flex-col">
        <div v-for="theme in colors" :key="theme">
          <ThemeVue @click="clickChangeTheme(theme)"
            :theme="theme" />
        </div>
      </div>
    </div>
    <FooterVue />
  </div>
</template>

<script setup>
import { onMounted } from 'vue';
import FooterVue from '@/components/FooterVue.vue';
import ThemeVue from '@/components/Theme/ThemeVue.vue';
import { storeToRefs } from 'pinia';
import { useStore } from '@/stores/store';

const store = useStore();
const { colors } = storeToRefs(store);
const { getColors, clickChangeTheme } = store;

onMounted(async() => {
  await getColors();
});
</script>

<style scoped>
</style>