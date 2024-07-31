<template>
  <div class="max-w-[500px] w-full h-full fixed top-0 bg-opacity-40 bg-black z-50 flex justify-center items-end pb-14" @click="handleClickClosePostCategoryModal()">
    <div class="w-[260px] min-w-[260px] h-auto bg-white rounded-2xl flex py-1" @click.stop>
      <div class="flex flex-col w-full">
        <div v-for="category in categories" :key="category" class="w-full py-2" :class="{ 'border-b' : category != 3 }">
          <div class="flex gap-4 items-center w-full px-5" @click="confirm(category)">
            <div class="w-5 h-5 rounded-full" :style="getBackgroundColor(category)"></div>
            <div class="text-lg">{{ category.categoryTitle }}</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useModalStore } from '@/stores/modalStore.js';
import { useStore } from '@/stores/store';
import { storeToRefs } from 'pinia';
import { onMounted } from 'vue';

const { handleClickClosePostCategoryModal } = useModalStore();
const { getCategories } = useStore();
const { categories, usingTheme } = storeToRefs(useStore());

const confirm = (category) => {
  handleClickClosePostCategoryModal();
};

const getBackgroundColor = (category) => {
  return { backgroundColor: usingTheme.value.colorList[category.categoryColor].colorCode }
};

onMounted(async () => {
  await getCategories();
});
</script>

<style lang="css" scoped>
</style>
