<template>
  <div class="max-w-[500px] w-full h-full fixed top-0 bg-opacity-40 bg-black z-50 flex justify-center items-center p-4" @click="handleClickCloseModal()">
    <div class="w-[340px] min-w-[320px] h-[540px] min-h-[400px] bg-white rounded-2xl flex flex-col items-center select-none p-5 justify-between" @click.stop>
      <div class="w-full">
        <div class="pb-4">{{ currentMonth }}월 {{ modalDate }}일 ({{ dayOfWeek }})</div>
        <div v-if="datePostDatas.length !== 0">
          <ModalPostVue v-for="post in datePostDatas"
            :key="post"
            :post="post" />
        </div>
      </div>
      <div @click="handleClickCategoryModal()" class="bg-[#EEEEEE] text-[#666666] w-full h-auto rounded-md p-4 text-sm">
        + 할 일을 추가하세요
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, watch } from 'vue';
import { storeToRefs } from 'pinia';
import { useModalStore } from '@/stores/modalStore.js';
import { useStore } from '@/stores/store';
import ModalPostVue from './Post/ModalPostVue.vue';
import { getDay } from 'date-fns';

const useModal = useModalStore();
const { datePostDatas, modalDate } = storeToRefs(useModal);
const { handleClickCloseModal, handleClickCategoryModal, handleClickPostModal } = useModal;
const { currentMonth, currentYear } = storeToRefs(useStore());

const type = ref("edit");

const daysOfWeek = ['일', '월', '화', '수', '목', '금', '토'];

const dayOfWeek = computed(() => {
  const date = new Date(currentYear.value, currentMonth.value - 1, modalDate.value);
  const day = getDay(date);
  return daysOfWeek[day];
});

watch([modalDate, currentMonth, currentYear], () => {
  dayOfWeek.value;
});
</script>

<style lang="css" scoped>
</style>
