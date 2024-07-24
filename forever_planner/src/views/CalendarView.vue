<template>
  <DateModal v-if="dateModalState" />
  <CategoryModal v-if="categoryModalState" />
  <PostModal v-if="postModalState" />
  <PostCategoryModal v-if="postCategoryModalState" />
  <ConfirmModal v-if="confirmModalState" />
  <div class="w-full h-screen flex flex-col justify-between">
    <div class="w-full h-full bg-[#f5f7fd] p-2 flex flex-col justify-end">
      <div class="text-2xl font-semibold p-3">7월</div>
      <CalendarVue class="w-full h-full"/>
    </div>
    <FooterVue />
  </div>
</template>

<script setup>
import CalendarVue from '@/components/Calendar/CalendarVue.vue'
import FooterVue from '@/components/FooterVue.vue';
import DateModal from '@/components/Calendar/DateModal.vue';
import CategoryModal from '@/components/Calendar/Category/CategoryModal.vue';
import PostModal from '@/components/Calendar/Post/PostModal.vue';
import PostCategoryModal from '@/components/Calendar/Category/PostCategoryModal.vue';
import ConfirmModal from '@/components/Calendar/ConfirmModal.vue';
import { storeToRefs } from 'pinia';
import { useModalStore } from '@/stores/modalStore.js';
import { onMounted, watchEffect } from 'vue';

const { dateModalState, categoryModalState, postModalState, postCategoryModalState, confirmModalState } = storeToRefs(useModalStore());

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

<style scoped>
</style>