<template>
  <div class="max-w-[500px] w-full h-full fixed top-0 bg-opacity-40 bg-black z-50 flex justify-center items-end p-4" @click="handleClickCloseCategoryModal()">
    <div class="w-full h-auto bg-white rounded-2xl flex flex-col items-center select-none p-5 justify-between" @click.stop>
      <div class="flex justify-between w-full p-2 text-lg">
        <div>카테고리 선택</div>
        <div v-if="!editMode" @click="clickEditMode" class="text-[#5f7ee3]">편집</div>
        <div v-else @click="clickEditMode" class="text-[#5f7ee3]">완료</div>
      </div>
      <div v-if="!editMode" class="flex flex-col w-full gap-2">
        <div v-for="(row, rowIndex) in chunkedCategories" :key="rowIndex" class="flex w-full gap-2">
          <div v-for="category in row" :key="category.id" class="flex-1">
            <div @click="clickMakePost()" class="w-full aspect-square bg-[#F8F8F8] rounded-2xl flex items-center justify-center">
              <div class="flex flex-col gap-2 items-center">
                <div class="w-[24px] h-[24px] rounded-full bg-[#a7c8f7]"></div>
                <div>{{ category.name }}</div>
              </div>
            </div>
          </div>
          <div v-for="i in (4 - row.length)" :key="`empty-${rowIndex}-${i}`" class="flex-1">
            <div class="w-full aspect-square bg-transparent"></div>
          </div>
        </div>
      </div>
      <div v-else class="flex flex-col w-full gap-2">
        <div v-for="(row, rowIndex) in chunkedEditCategories" :key="rowIndex" class="flex w-full gap-2">
          <div v-for="category in row" :key="category.id || `plus-${rowIndex}`" class="flex-1">
            <div
              v-if="category.id"
              class="w-full aspect-square bg-[#F8F8F8] rounded-2xl flex items-center justify-center"
              @click="clickMoveCategory()"
            >
              <div class="flex flex-col gap-1.5 items-center">
                <div class="icon-color">
                  <i class="fa-solid fa-square-pen w-[24px] h-[24px]"></i>
                </div>
                <div>{{ category.name }}</div>
              </div>
            </div>
            <div v-else class="w-full aspect-square bg-[#F8F8F8] rounded-2xl flex items-center justify-center" @click="clickMoveCategory()">
              <div class="flex flex-col gap-2 items-center">
                <div class="w-[24px] h-[24px] rounded-full bg-[#444444] text-white flex items-center justify-center">
                  <i class="fa-solid fa-plus"></i>
                </div>
              </div>
            </div>
          </div>
          <div v-for="i in (4 - row.length)" :key="`empty-edit-${rowIndex}-${i}`" class="flex-1">
            <div class="w-full aspect-square bg-transparent"></div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>



<script setup>
import { ref, computed } from 'vue';
import { useModalStore } from '@/stores/modalStore.js';
import { useRouter } from 'vue-router';

const router = useRouter();
const type = ref("add");
const { handleClickCloseCategoryModal, handleClickPostModal } = useModalStore();

const editMode = ref(false);

const clickEditMode = () => {
  editMode.value = !editMode.value;
};

const clickMoveCategory = () => {
  router.push({ name: 'category' });
};

const clickMakePost = () => {
  handleClickCloseCategoryModal();
  handleClickPostModal(type.value);
};

const categories = ref([
  { id: 1, name: '일상' },
  { id: 2, name: '일상' },
  { id: 3, name: '일상' },
  { id: 4, name: '일상' },
  { id: 5, name: '일상' },
  { id: 6, name: '일상' },
  { id: 7, name: '일상' },
  { id: 8, name: '일상' },
]);

const chunkedCategories = computed(() => {
  const chunks = [];
  for (let i = 0; i < categories.value.length; i += 4) {
    chunks.push(categories.value.slice(i, i + 4));
  }
  return chunks;
});

const chunkedEditCategories = computed(() => {
  const chunks = [];
  for (let i = 0; i < categories.value.length; i += 4) {
    chunks.push(categories.value.slice(i, i + 4));
  }
  if (chunks.length > 0 && chunks[chunks.length - 1].length === 4) {
    chunks.push([{}]);
  } else if (chunks.length > 0) {
    chunks[chunks.length - 1].push({});
  }
  return chunks;
});
</script>

<style lang="css" scoped>
.icon-color {
  color: #a7c8f7;
}
</style>
