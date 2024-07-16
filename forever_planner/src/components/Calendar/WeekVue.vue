<template>
  <div class="flex justify-between py-3 text-2xs">
    <div v-for="week in weeks" :key="week" class="w-full flex items-center justify-center">{{ week }}</div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
const weeks = ref(["일", "월", "화", "수", "목", "금", "토"])
</script>

<style scoped>
</style>
