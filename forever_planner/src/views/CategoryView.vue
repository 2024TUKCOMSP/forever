<template>
  <div class="w-full h-screen flex flex-col justify-between bg-[#f5f7fd]">
    <div class="w-full p-6 flex flex-col gap-8">
      <div class="w-full">
        <div @click="clickGoBehind()">
         <i class="fa-solid fa-chevron-left h-[30px] w-[30px]"></i>
        </div>
      </div>
      <input class="w-full h-16 rounded-2xl p-4 text-2xl focus:outline-none" v-model="title" placeholder="카테고리를 입력하세요" maxlength="10"/>
      <div class="bg-white rounded-2xl p-6 flex flex-col items-center">
        <div class="text-xl flex items-center">{{ usingTheme.themeTitle }}</div>
        <div class="flex flex-col gap-4 w-full p-6">
          <div v-for="line in 2" :key="line" class="flex justify-between w-full">
            <div v-for="color in 4" :key="color" class="w-12 h-12 rounded-full flex items-center justify-center" :style="getColor(line, color)" @click="selectCategoryColor((line - 1) * 4 + (color - 1))">
              <div v-if="isSelected((line - 1) * 4 + (color - 1))" class="flex items-center justify-center">
                <i class="fa-regular fa-circle w-10 h-10"></i>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div @click="saveCategory()" class="px-6 py-12">
      <div class="w-full h-16 bg-[#5f7ee3] text-white rounded-2xl flex justify-center items-center text-xl">저장</div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { useStore } from '@/stores/store';
import { storeToRefs } from 'pinia';

const store = useStore();
const { getColors, createCategory, editCurrentCategory, deleteCategory } = store;
const { usingTheme, editCategory } = storeToRefs(store);
const router = useRouter();
const selectedCategoryNum = ref(-1);
const title = ref("");

const clickGoBehind = () => {
  router.go(-1);
  editCategory.value = [];
};

};

const saveCategory = () => {
  if(editCategory.value.categoryId) editCurrentCategory(editCategory.value.categoryId, selectedCategoryNum.value, title.value);
  else createCategory(selectedCategoryNum.value, title.value);
  router.go(-1);
  editCategory.value = [];
};

const getColor = (line, num) => {
  return { background: usingTheme.value.colorList[(line - 1) * 4 + (num - 1)].colorCode, color: "#ffffff" }
};

const selectCategoryColor = (num) => {
  selectedCategoryNum.value = num;
};

const isSelected = (num) => {
  return num === selectedCategoryNum.value;
};

onMounted(async () => {
  await getColors();
  if(editCategory.value.categoryId) {
    selectedCategoryNum.value = editCategory.value.categoryColor;
    title.value = editCategory.value.categoryTitle;
  }
});
</script>

<style scoped>
</style>