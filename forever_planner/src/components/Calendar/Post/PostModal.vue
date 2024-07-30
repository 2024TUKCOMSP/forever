<template>
  <div class="max-w-[500px] w-full h-full fixed top-0 bg-opacity-40 bg-black z-50 flex flex-col justify-end" @click="handleClickClosePostModal()">
    <div v-if="postModalType == 'edit'" class="p-4" @click.stop>
      <div @click="handleClickConfirmModal()" class="w-10 h-10 bg-[#FF2200] rounded-xl flex items-center justify-center trash-color">
        <i class="fa-solid fa-trash-can"></i>
      </div>
    </div>
    <div class="flex flex-col w-full">
      <div class="w-full h-auto rounded-t-2xl" :style="getBackgroundColor()" @click.stop>
        <div class="flex flex-col items-center select-none px-6 py-4 justify-between gap-2 w-full h-full rounded-t-2xl bg-[#FFFFFFBB]">
          <input placeholder="할 일을 입력하세요" v-model="postTitle" class="w-full bg-[#FFFFFF00] focus:outline-none text-lg" />
            <textarea v-if="isContentActive" placeholder="메모를 입력하세요" v-model="content" class="w-full bg-[#FFFFFF00] focus:outline-none resize-none" maxlength="70"></textarea>
            <div class="flex justify-between w-full pt-2">
              <div class="flex gap-4 items-center">
                <div class="flex items-center" :style="getCalendarIconColor()" @click="clickCalendarButton()">
                  <i class="fa-solid fa-calendar-day w-5 h-5"></i>
                </div>
                <div class="text-[#00000050]">{{ postMonth }}월 {{ postDate }}일 ({{ dayOfWeek }})</div>
                <div class="flex items-center" :style="getContentIconColor()" @click="clickContentButton()">
                  <i class="fa-solid fa-note-sticky w-5 h-5"></i>
                </div>
                <div class="text-[#00000050]" @click="handleClickCategory()">{{ category }}</div>
              </div>
              <div class="flex items-center icon-color" @click="submit()">
                <i class="fa-solid fa-paper-plane w-5 h-5"></i>
              </div>
            </div>
        </div>
      </div>
      <div v-if="isCalendarActive" class="w-full" @click.stop>
        <PostCalendar />
      </div>
    </div>
  </div>
</template>

<script setup>
import PostCalendar from './PostCalendar.vue';
import { useModalStore } from '@/stores/modalStore.js';
import { storeToRefs } from 'pinia';
import { useStore } from '@/stores/store.js';
import { onMounted, ref, computed, watch } from 'vue';
import { getDay } from 'date-fns';

const { handleClickClosePostModal, handleClickPostCategoryModal, handleClickConfirmModal } = useModalStore();
const { postModalType, categoryColor, postData, modalDate } = storeToRefs(useModalStore());
const { currentMonth, currentYear, postMonth, postYear, postDate } = storeToRefs(useStore());

const isCalendarActive = ref(false);
const isContentActive = ref(false);
const postTitle = ref("");
const content = ref("");
const category = ref("");

const clickCalendarButton = () => {
  isCalendarActive.value = !isCalendarActive.value;
  isContentActive.value = false;
};

const clickContentButton = () => {
  isContentActive.value = !isContentActive.value;
  isCalendarActive.value = false;
};

const handleClickCategory = () => {
  isContentActive.value = false;
  isCalendarActive.value = false;
  handleClickPostCategoryModal();
};

const submit = () => {
  handleClickClosePostModal();
};

const getBackgroundColor = () => {
  return { backgroundColor: categoryColor.value };
};

const getCalendarIconColor = () => {
  if(isCalendarActive.value) return { color: categoryColor.value, transition: 'color 0.1s' };
  else return { color: '#00000050', transition: 'color 0.1s' };
};

const getContentIconColor = () => {
  if(isContentActive.value) return { color: categoryColor.value, transition: 'color 0.1s' };
  else return { color: '#00000050', transition: 'color 0.1s' };
};

const daysOfWeek = ['일', '월', '화', '수', '목', '금', '토'];

const dayOfWeek = computed(() => {
  const date = new Date(postYear.value, postMonth.value - 1, postDate.value);
  const day = getDay(date);
  return daysOfWeek[day];
});

watch([postDate, postMonth, postYear], () => {
  dayOfWeek.value;
});

onMounted(() => {
  postMonth.value = currentMonth.value;
  postYear.value = currentYear.value;
  postDate.value = modalDate.value;
  if(postData.value) {
    postTitle.value = postData.value.title;
    content.value = postData.value.content;
    category.value = postData.value.category.categoryTitle;
  };
});
</script>

<style lang="css" scoped>
.trash-color {
  color: #ffffff;
}
</style>
