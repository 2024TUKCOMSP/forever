<template>
  <div class="max-w-[500px] w-full h-full fixed top-0 bg-opacity-40 bg-black z-50 flex flex-col justify-end" @click="handleClickClosePostModal()">
    <div v-if="postModalType == 'edit'" class="p-4" @click.stop>
      <div @click="handleClickConfirmModal()" class="w-10 h-10 bg-[#FF2200] rounded-xl flex items-center justify-center trash-color">
        <i class="fa-solid fa-trash-can"></i>
      </div>
    </div>
    <div class="flex flex-col w-full">
      <div class="w-full h-auto bg-[#e4eefc] rounded-t-2xl flex flex-col items-center select-none px-6 py-4 justify-between gap-2" @click.stop>
        <input placeholder="할 일을 입력하세요" v-model="postTitle" class="w-full bg-[#e4eefc] focus:outline-none text-lg" />
        <textarea v-if="isContentActive" placeholder="메모를 입력하세요" v-model="content" class="w-full bg-[#e4eefc] focus:outline-none resize-none" maxlength="70"></textarea>
        <div class="flex justify-between w-full pt-2">
          <div class="flex gap-4 items-center">
            <div class="flex items-center" :class="isCalendarActive ? 'clicked-icon-color' : 'icon-color'" @click="clickCalendarButton()">
              <i class="fa-solid fa-calendar-day w-5 h-5"></i>
            </div>
            <div class="text-[#00000050]">7월 12일 (금)</div>
            <div class="flex items-center" :class="isContentActive ? 'clicked-icon-color' : 'icon-color'" @click="clickContentButton()">
              <i class="fa-solid fa-note-sticky w-5 h-5"></i>
            </div>
            <div class="text-[#00000050]">일상</div>
          </div>
          <div class="flex items-center icon-color" @click="submit()">
            <i class="fa-solid fa-paper-plane w-5 h-5"></i>
          </div>
        </div>
      </div>
      <div v-if="isCalendarActive" class="w-full">
        <PostCalendar />
      </div>
    </div>
  </div>
</template>

<script setup>
import PostCalendar from './PostCalendar.vue';
import { useModalStore } from '@/stores/modalStore.js';
import { storeToRefs } from 'pinia';
import { ref } from 'vue'

const { handleClickClosePostModal } = useModalStore();
const { postModalType } = storeToRefs(useModalStore());

const isCalendarActive = ref(false);
const isContentActive = ref(false);
const postTitle = ref("방학");
const content = ref("");

const clickCalendarButton = () => {
  isCalendarActive.value = !isCalendarActive.value;
  isContentActive.value = false;
};

const clickContentButton = () => {
  isContentActive.value = !isContentActive.value;
  isCalendarActive.value = false;
};

const submit = () => {
  handleClickClosePostModal();
};
</script>


<style lang="css" scoped>
.icon-color {
  color: #00000050;
  transition: color 0.1s;
}

.clicked-icon-color {
  color: #a7c8f7;
  transition: color 0.1s;
}

.trash-color {
  color: #ffffff;
}
</style>
