import { ref } from 'vue';
import { defineStore } from 'pinia';

export const useStore = defineStore('store', () => {
  const isClicked = ref('diary');
  const currentMonth = ref(new Date().getMonth() + 1);
  const isFinished = ref(false);

  const changeFinishedState = () => {
    isFinished.value = !isFinished.value;
  };

  const changeMonth = (month) => {
    currentMonth.value = month;
  };

  return {
    isClicked,
    currentMonth,
    isFinished,
    changeMonth,
    changeFinishedState,
  };
});
