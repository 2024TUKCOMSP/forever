<template>
  <div class="bg-white w-full rounded-2xl flex flex-col p-6 gap-4">
    <div class="flex justify-between">
      <div>{{ theme.themeTitle }}</div>
      <div class="text-[#999999]">적용중</div>
    </div>
    <div class="flex justify-between px-2">
      <div v-for="color in theme.colorList" :key="color">
        <div class="w-8 h-8 rounded-full" :style="{ backgroundColor: color }"></div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue';

const props = defineProps({
  isSelected: {
    type: Boolean,
    default: true,
  },
  theme: {
    type: Object,
    required: true,
  }
});

onMounted(() => {
});
</script>

<style></style>
