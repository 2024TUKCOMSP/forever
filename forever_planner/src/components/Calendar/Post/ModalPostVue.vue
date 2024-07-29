<template>
  <div class="px-0.5 py-1 w-full">
    <div class="bg-[#de9bac] w-full h-[48px] rounded-md text-xs flex justify-end relative">
      <div class="h-full bg-[#ffffffbb] flex items-center pr-4" :class="isFinished ? 'w-full rounded-md' : 'w-[98%] rounded-r-md'">
        <div class="flex w-full h-full" :class="isFinished ? 'px-2' : 'px-0.5'">
          <div class="flex flex-col pl-2 justify-center grow" @click="handleClickPostModal(type)">
            <div class="text-2xs text-[#999999]">일상</div>
            <div>방학</div>
          </div>
        </div>
        <div v-if="isFinished" @click="changeFinishedState()" class="flex items-center">
          <i class="fa-solid fa-check w-4 h-4 icon-color"></i>
        </div>
        <div v-else class="w-4 h-4 border border-[#de9bac] rounded-sm" @click="changeFinishedState()"></div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { storeToRefs } from 'pinia';
import { useStore } from '@/stores/store';
import { useModalStore } from '@/stores/modalStore.js';

const store = useStore();
const { isFinished } = storeToRefs(store);
const { changeFinishedState } = store;
const { handleClickPostModal } = useModalStore();

const type = ref("edit")
</script>

<style scoped>
.icon-color {
  color: #de9bac;
}
</style>
