import { ref } from 'vue';
import { defineStore } from 'pinia';

export const useModalStore = defineStore('modalStore', () => {
  const dateModalState = ref(false);

  const handleClickDateModal = () => {
    dateModalState.value = true;
  };

  const handleClickCloseModal = () => {
    dateModalState.value = false;
  };

  return {
    dateModalState,
    handleClickDateModal,
    handleClickCloseModal,
  };
});
