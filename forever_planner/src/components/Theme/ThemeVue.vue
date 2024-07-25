<template>
  <div class="bg-white w-full rounded-2xl flex flex-col p-6 gap-4">
    <div class="flex justify-between">
      <div>Planit 3.0</div>
      <div v-if="props.isSelected" class="text-[#999999]">적용중</div>
    </div>
    <div class="flex justify-between px-2">
      <div v-for="color in 8" :key="color">
        <div class="w-8 h-8 rounded-full bg-[#a7c8f7]"></div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const props = defineProps({
  isSelected: {
    type: Boolean,
    default: false
  }
});
</script>

<style></style>