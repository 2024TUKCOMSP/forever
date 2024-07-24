import { ref } from 'vue';
import { defineStore } from 'pinia';

export const useModalStore = defineStore('modalStore', () => {
  const dateModalState = ref(false);
  const categoryModalState = ref(false);

  const handleClickDateModal = () => {
    dateModalState.value = true;
  };

  const handleClickCloseModal = () => {
    dateModalState.value = false;
  };

  const handleClickCategoryModal = () => {
    categoryModalState.value = true;
  };

  const handleClickCloseCategoryModal = () => {
    categoryModalState.value = false;
  };

  return {
    dateModalState,
    handleClickDateModal,
    handleClickCloseModal,
    handleClickCloseCategoryModal,
    handleClickCategoryModal,
    categoryModalState
  };
});
