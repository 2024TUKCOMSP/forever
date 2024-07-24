import { ref } from 'vue';
import { defineStore } from 'pinia';

export const useModalStore = defineStore('modalStore', () => {
  const dateModalState = ref(false);
  const categoryModalState = ref(false);
  const postModalState = ref(false);
  const postCategoryModalState = ref(false);

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

  const handleClickPostModal = () => {
    postModalState.value = true;
  };

  const handleClickClosePostModal = () => {
    postModalState.value = false;
  };

  const handleClickPostCategoryModal = () => {
    postCategoryModalState.value = true;
  };

  const handleClickClosePostCategoryModal = () => {
    postCategoryModalState.value = false;
  };

  return {
    dateModalState,
    handleClickDateModal,
    handleClickCloseModal,
    handleClickCloseCategoryModal,
    handleClickCategoryModal,
    categoryModalState,
    postModalState,
    handleClickPostModal,
    handleClickClosePostModal,
    postCategoryModalState,
    handleClickPostCategoryModal,
    handleClickClosePostCategoryModal,
  };
});
