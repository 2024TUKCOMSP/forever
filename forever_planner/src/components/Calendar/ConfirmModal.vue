<template>
  <div class="max-w-[500px] w-full h-full fixed top-0 bg-opacity-40 bg-black z-50 flex justify-center items-center p-4" @click="handleClickCloseConfirmModal()">
    <div class="w-[260px] min-w-[260px] h-[200px] min-h-[200px] bg-white rounded-2xl flex flex-col p-4" @click.stop>
      <div class="w-full h-3/4 flex items-center justify-center">정말 삭제하시겠습니까?</div>
      <div class="flex h-1/4 justify-between">
        <div class="px-10 bg-[#F6F6F6] h-full flex items-center rounded-xl" @click="handleClickCloseConfirmModal()">취소</div>
        <div class="px-10 bg-[#FF2200] text-white h-full flex items-center rounded-xl" @click="handleClickDelete()">삭제</div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useModalStore } from '@/stores/modalStore.js';

const { handleClickCloseConfirmModal, handleClickClosePostModal } = useModalStore();

const handleClickDelete = () => {
  handleClickCloseConfirmModal();
  handleClickClosePostModal();
};
</script>

<style lang="css" scoped>
</style>
