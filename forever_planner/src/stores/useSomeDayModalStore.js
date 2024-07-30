//언젠가 할 일 ㅇ따로 구현하려다, 오류가 너무 심하게 나서 롤백함.

import { ref } from 'vue';
import { defineStore } from 'pinia';

export const useSomeDayModalStore = defineStore('modalStore', () => {
  const dateModalState = ref(false);
  const categoryModalState = ref(false);
  const someDayPostModalState = ref(false);
  const someDayPostCategoryModalState = ref(false);
  const someDayConfirmModalState = ref(false);
  const someDayPostCalendatState = ref(false);
  const postModalType = ref("");

  const handleClickDateModal = (date) => {
    if (date) dateModalState.value = true;
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

  const handleClickPostModal = (type) => {
    postModalType.value = type;
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

  const handleClickConfirmModal = () => {
    confirmModalState.value = true;
  };

  const handleClickCloseConfirmModal = () => {
    confirmModalState.value = false;
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
    confirmModalState,
    handleClickConfirmModal,
    handleClickCloseConfirmModal,
    postModalType,
  };
});
