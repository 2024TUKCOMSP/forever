<template>
  <div class="max-w-[500px] w-full h-full fixed top-0 bg-opacity-40 bg-black z-50 flex justify-center items-end p-4" @click="handleClickCloseCategoryModal()">
    <div class="w-full h-auto bg-white rounded-2xl flex flex-col items-center select-none p-5 justify-between" @click = "clickCloseFunc()">
      <div class="flex justify-between w-full p-2 text-lg" >
        <div>카테고리 선택</div>
        <div v-if="!editMode" @click="clickEditMode" class="text-[#5f7ee3]">편집</div>
        <div v-else @click="clickEditMode" class="text-[#5f7ee3]">완료</div>
      </div>
      <div v-if="!editMode" class="flex flex-col w-full gap-2">
        <div v-for="(row, rowIndex) in chunkedCategories" :key="rowIndex" class="flex w-full gap-2">
          <div v-for="categories in row" :key="categories.categoryId" class="flex-1">
            <div @click="clickMakePost(categories)" class="w-full aspect-square bg-[#F8F8F8] rounded-2xl flex items-center justify-center">
              <div class="flex flex-col gap-2 items-center">
                <div class="w-[24px] h-[24px] rounded-full" :style="getBackgroundColor(categories)"></div>
                <div>{{ categories.categoryTitle }}</div>
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
          <div v-for="categories in row" :key="categories.categoryId || `plus-${rowIndex}`" class="flex-1">
            <div
              v-if="categories.categoryId"
              class="w-full aspect-square bg-[#F8F8F8] rounded-2xl flex items-center justify-center"
              @click="clickEditCategory(categories)"
            >
              <div class="flex flex-col gap-1.5 items-center">
                <div :style="getIconColor(categories)">
                  <i class="fa-solid fa-square-pen w-[24px] h-[24px]"></i>
                </div>
                <div>{{ categories.categoryTitle }}</div>
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
import { ref, computed, onMounted } from 'vue';
import { useModalStore } from '@/stores/modalStore.js';
import { useStore } from '@/stores/store';
import { storeToRefs } from 'pinia';
import { useRouter } from 'vue-router';
import { defineProps } from 'vue';

const router = useRouter();
const type = ref("add");
const { handleClickCloseCategoryModal, handleClickPostModal } = useModalStore();
const { currentCategory } = storeToRefs(useModalStore());
const { getCategories } = useStore();
const { categories, usingTheme, currentCategoryId, editCategory, isSomeday } = storeToRefs(useStore());

const editMode = ref(false);
const props = defineProps(['editMode']);

const clickCloseFunc = () => {
  if(props.editMode != null && editMode.value == false){
    //console.log(props.editMode + "" + editMode.value );
    clickEditMode();
  }else{
    //console.log(props.editMode + "" + editMode.value );
    event.stopPropagation();
  }
}

const clickEditMode = () => {
  if(props.editMode != null){
    router.push({name: 'setting'});
    //console.log("왜안됨");
    //handleClickCloseCategoryModal();
    //완료를 누를 때 모달이 닫히도록 수정하고 싶다면 이 곳에 코드를 추가하면 됨
    //이 곳은 settingView.vue에서 연 게 아니라면 열리지 않음을 확인함 
    //코드 중 어떤 function이 모달을 지우는 지 알지 못하겠음.. 
  }
    editMode.value = !editMode.value;
};

const clickMoveCategory = () => {
  router.push({ name: 'category' });
};

const clickMakePost = (category) => {
  currentCategory.value = category;
  currentCategoryId.value = category.categoryId;
  handleClickCloseCategoryModal();
  handleClickPostModal(type.value, getColor(category));
};

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

const getBackgroundColor = (category) => {
  //console.log(usingTheme.value.colorList[category.categoryColor].colorCode);
  return { backgroundColor : usingTheme.value.colorList[category.categoryColor].colorCode };
};

const getIconColor = (category) => {
  return { color : usingTheme.value.colorList[category.categoryColor].colorCode };
};

const getColor = (category) => {
  return usingTheme.value.colorList[category.categoryColor].colorCode;
};

const clickEditCategory = async (category) => {
  editCategory.value = category;
  await clickMoveCategory();
};

onMounted(() => {
  getCategories();
  if( props != null ){
    //console.log("edit mode: "+ props.editMode);
    editMode.value = props.editMode;
  }
 // console.log(props);
});
</script>

<style lang="css" scoped>
</style>
