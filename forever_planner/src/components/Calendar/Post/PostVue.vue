<template>
  <div class="p-0.5 w-full">
    <div class="bg-[#de9bac] justify-end w-full rounded text-2xs flex h-full">
      <div class="h-full bg-[#ffffffBB]" :class="isFinished ? 'w-full rounded' : 'w-[95%] rounded-r'">
        <div class="w-full p-[0.5px] flex items-center justify-center">방학</div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { storeToRefs } from 'pinia';
import { useStore } from '@/stores/store';

const store = useStore();
const { isFinished } = storeToRefs(store);
</script>

<style scoped>

</style>