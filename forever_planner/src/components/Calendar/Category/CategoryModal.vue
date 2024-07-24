<template>
  <div class="max-w-[500px] w-full h-full fixed top-0 bg-opacity-40 bg-black z-50 flex justify-center items-end p-4" @click="handleClickCloseCategoryModal()">
    <div class="w-full h-auto bg-white rounded-2xl flex flex-col items-center select-none p-5 justify-between" @click.stop>
      <div class="flex justify-between w-full p-2 text-lg">
        <div>카테고리 선택</div>
        <div v-if="!editMode" @click="clickEditMode" class="text-[#5f7ee3]">편집</div>
        <div v-else @click="clickEditMode" class="text-[#5f7ee3]">완료</div>
      </div>
      <div v-if="!editMode" class="flex w-full gap-2">
        <div v-for="category in 3" :key="category">
          <CategoryVue />
        </div>
      </div>
      <div v-else class="flex w-full gap-2">
        <div v-for="category in 3" :key="category">
          <CategoryEditVue @click="clickMoveCategory()"/>
        </div>
        <CategoryAddVue @click="clickMoveCategory()"/>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useModalStore } from '@/stores/modalStore.js';
import { useRouter } from 'vue-router';
import CategoryVue from './CategoryVue.vue';
import CategoryAddVue from './CategoryAddVue.vue';
import CategoryEditVue from './CategoryEditVue.vue';

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
</script>


<style lang="css" scoped>
</style>
