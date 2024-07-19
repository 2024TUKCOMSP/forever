<script setup>
import DateModal from '@/components/Calendar/DateModal.vue';
import { RouterView } from 'vue-router';
import { useModalStore } from '@/stores/modalStore.js';
import { storeToRefs } from 'pinia';
import { onMounted, watchEffect } from 'vue';

const { dateModalState } = storeToRefs(useModalStore());

const handleStopScroll = () => {
  if (dateModalState.value) document.documentElement.style.overflow = 'hidden';
  else document.documentElement.style.overflow = 'auto';
};

watchEffect(() => {
  handleStopScroll();
});

onMounted(() => {
  window.scrollTo(0, 0);
});
</script>

<template>
  <RouterView />
  <DateModal v-if="dateModalState" />
</template>

<style scoped></style>
