<template>
  <div class="w-full" :style="getBackgroundColor()">
    <div class="relative w-full bg-[#FFFFFFBB] gap-1.5 flex flex-col py-4">
      <div class="absolute inset-0 bg-[#00000008]"></div>
      <div class="w-full flex justify-center pb-2">
        <div class="text-lg font-semibold">7월 2024</div>
      </div>
      <div class="flex">
        <div v-for="week in weeks" :key="week" class="w-[14.2%] text-center text-sm">{{ week }}</div>
      </div>
      <div v-for="week in 6" :key="week" class="flex justify-evenly text-xl">
        <div v-for="day in 7" :key="day" class="w-[14.2%] flex justify-center">
          <div :class="{ 'rounded-full bg-black text-white h-full aspect-square text-center font-semibold': week == 2 && day == 5 }">{{ day }}</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useModalStore } from '@/stores/modalStore';
import { storeToRefs } from 'pinia';

const { categoryColor } = storeToRefs(useModalStore());
const weeks = ["일", "월", "화", "수", "목", "금", "토"];

const getBackgroundColor = () => {
  return { backgroundColor: categoryColor.value };
};
</script>

<style scoped>
</style>
