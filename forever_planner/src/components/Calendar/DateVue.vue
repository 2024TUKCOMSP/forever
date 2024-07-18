<template>
  <div class="flex flex-col h-full justify-between text-2xs">
    <div v-for="week in 5" :key="week" class="flex w-full h-full">
      <div v-for="date in 7" :key="date" class="w-full h-full flex flex-col items-center justify-start" @click="handleClickDateModal()">
        <div class="pb-0.5">{{ date }}</div>
        <PostVue />
        <FinishedPostVue />
      </div>
    </div>
  </div>
</template>

<script setup>
import PostVue from './PostVue.vue';
import FinishedPostVue from '@/components/FinishiedPostVue.vue'
import { useModalStore } from '@/stores/modalStore.js';

const { handleClickDateModal } = useModalStore();
</script>

<style scoped>
</style>
