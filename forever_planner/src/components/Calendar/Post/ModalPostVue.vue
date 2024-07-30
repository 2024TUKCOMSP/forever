<template>
  <div class="px-0.5 py-1 w-full">
    <div class="w-full h-[48px] rounded-md text-xs flex justify-end relative" :style="getBackgroundColor()">
      <div class="h-full bg-[#ffffffbb] flex items-center pr-4" :class="post.isFinished ? 'w-full rounded-md' : 'w-[98%] rounded-r-md'">
        <div class="flex w-full h-full" :class="post.isFinished ? 'px-2' : 'px-0.5'">
          <div class="flex flex-col pl-2 justify-center grow" @click="handleClickPostModal(type)">
            <div class="text-2xs text-[#999999]">{{ post.category.categoryTitle }}</div>
            <div>{{ post.title }}</div>
          </div>
        </div>
        <div v-if="post.isFinished" @click="changeFinishedState(post.isFinished, post.postId)" class="flex items-center">
          <i class="fa-solid fa-check w-4 h-4" :style="getIconColor()"></i>
        </div>
        <div v-else class="w-4 h-4 border rounded-sm" :style="getBorderColor()" @click="changeFinishedState(post.isFinished, post.postId)"></div>
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
const { usingTheme } = storeToRefs(store);
const { changeFinishedState } = store;
const { handleClickPostModal } = useModalStore();

const type = ref("edit");

const props = defineProps({
  post: {
    type: Object,
    required: true
  },
});

const getBackgroundColor = () => {
  return { backgroundColor: usingTheme.value.colorList[props.post.category.categoryColor].colorCode };
};

const getBorderColor = () => {
  return { borderColor: usingTheme.value.colorList[props.post.category.categoryColor].colorCode };
};

const getIconColor = () => {
  return { color: usingTheme.value.colorList[props.post.category.categoryColor].colorCode };
};
</script>

<style scoped>
</style>
