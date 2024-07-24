import { ref } from 'vue';
import { defineStore } from 'pinia';

export const useStore = defineStore('store', () => {
  const isClicked = ref('diary');

  return {
    isClicked,
  };
});
