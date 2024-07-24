<template>
  <div class="max-w-[500px] w-full h-full fixed top-0 bg-opacity-40 bg-black z-50 flex justify-center items-end pb-14" @click="handleClickClosePostCategoryModal()">
    <div class="w-[260px] min-w-[260px] h-auto bg-white rounded-2xl flex py-1" @click.stop>
      <div class="flex flex-col w-full">
        <div v-for="category in 3" :key="category" class="w-full py-2" :class="{ 'border-b' : category != 3 }">
          <PostCategory @click="confirm()"/>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import PostCategory from './PostCategory.vue';
import { useModalStore } from '@/stores/modalStore.js';

const { handleClickClosePostCategoryModal } = useModalStore();

const confirm = () => {
  handleClickClosePostCategoryModal();
};

</script>

<style lang="css" scoped>
</style>
