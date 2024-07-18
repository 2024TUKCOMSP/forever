<template>
  <div class="w-full items-center h-12 bg-[#f5f7fd] flex justify-around">
    <div :class="isClicked === 'home' ? 'clicked-icon-color' : 'icon-color'" @click="clickHomeButton">
      <i class="w-6 h-6 fa-solid fa-house"></i>
    </div>
    <div :class="isClicked === 'diary' ? 'clicked-icon-color' : 'icon-color'" @click="clickDiaryButton">
      <i class="w-6 h-6 fa-solid fa-calendar-day"></i>
    </div>
    <div :class="isClicked === 'theme' ? 'clicked-icon-color' : 'icon-color'" @click="clickThemeButton">
      <i class="w-6 h-6 fa-solid fa-palette"></i>
    </div>
  </div>
</template>

<script setup>
import { storeToRefs } from 'pinia';
import { useStore } from '@/stores/store.js';
import { useRouter } from 'vue-router';

const store = useStore();
const { isClicked } = storeToRefs(store);
const router = useRouter();

const clickHomeButton = () => {
  isClicked.value = 'home';
  router.push({ name: 'home' });
};

const clickDiaryButton = () => {
  isClicked.value = 'diary';
  router.push({ name: 'calendar' });
};

const clickThemeButton = () => {
  isClicked.value = 'theme';
};
</script>

<style scoped>
.icon-color {
  color: #d3d3d3;
  transition: color 0.1s;
}

.clicked-icon-color {
  color: #878787;
  transition: color 0.1s;
}
</style>