import { ref } from 'vue';
import { defineStore } from 'pinia';

export const useModalStore = defineStore('modalStore', () => {
  const dateModalState = ref(false);
  const categoryModalState = ref(false);
  const postModalState = ref(false);
  const postCategoryModalState = ref(false);
  const confirmModalState = ref(false);
  const postModalType = ref("");
  const datePostDatas = ref({});
  const modalDate = ref(0);
  const categoryColor = ref("");
  const postData = ref([]);

  const handleClickDateModal = (date, data) => {
    datePostDatas.value = data;
    if (date) dateModalState.value = true;
    modalDate.value = date;
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

  const handleClickPostModal = (type, color, data) => {
    categoryColor.value = color;
    postModalType.value = type;
    postData.value = data;
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
    datePostDatas,
    modalDate,
    categoryColor,
    postData,
  };
});
