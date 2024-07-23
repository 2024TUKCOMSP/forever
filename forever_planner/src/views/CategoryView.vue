<template>
  <div class="w-full h-screen flex flex-col justify-between bg-[#f5f7fd]">
    <div class="w-full p-6 flex flex-col gap-8">
      <div class="w-full">
        <div @click="clickGoBehind()">
         <i class="fa-solid fa-chevron-left h-[30px] w-[30px]"></i>
        </div>
      </div>
      <input class="w-full h-16 rounded-2xl p-4 text-2xl focus:outline-none" placeholder="카테고리를 입력하세요"/>
      <div class="bg-white rounded-2xl p-6 flex flex-col items-center">
        <div class="flex items-center gap-12">
          <i class="fa-solid fa-chevron-left w-[20px] h-[20px]"></i>
          <div class="text-xl">Planit 3.0</div>
          <i class="fa-solid fa-chevron-right w-[20px] h-[20px]"></i>
        </div>
        <div class="flex flex-col gap-4 w-full p-6">
          <div v-for="line in 2" :key="line" class="flex justify-between w-full">
            <div v-for="color in 4" :key="color" class="w-[52px] h-[52px] rounded-full bg-[#a7c8f7]"></div>
          </div>
        </div>
      </div>
    </div>
    <div @click="saveCategory()" class="px-6 py-12">
      <div class="w-full h-16 bg-[#5f7ee3] text-white rounded-2xl flex justify-center items-center text-xl">저장</div>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router';

const router = useRouter();

const clickGoBehind = () => {
  router.go(-1);
};

const saveCategory = () => {
  router.go(-1);
};
</script>

<style scoped>
</style>