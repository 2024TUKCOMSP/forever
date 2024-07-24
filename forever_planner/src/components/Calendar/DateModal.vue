<template>
  <div class="max-w-[500px] w-full h-full fixed top-0 bg-opacity-40 bg-black z-50 flex justify-center items-center p-4" @click="handleClickCloseModal()">
    <div class="w-[340px] min-w-[320px] h-[540px] min-h-[400px] bg-white rounded-2xl flex flex-col items-center select-none p-5 justify-between" @click.stop>
      <div class="w-full">
        <div class="pb-4">7월 12일 (금)</div>
        <ModalPostVueVue @click="handleClickPostModal()" />
        <ModalFinishedPostVue @click="handleClickPostModal()" />
      </div>
      <div @click="handleClickCategoryModal()" class="bg-[#EEEEEE] text-[#666666] w-full h-auto rounded-md p-4 text-sm">
        + 할 일을 추가하세요
      </div>
    </div>
  </div>
</template>

<script setup>
import { useModalStore } from '@/stores/modalStore.js';
import ModalPostVueVue from './Post/ModalPostVue.vue';
import ModalFinishedPostVue from './Post/ModalFinishedPostVue.vue';

const { handleClickCloseModal, handleClickCategoryModal, handleClickPostModal } = useModalStore();

</script>


<style lang="css" scoped>
</style>
