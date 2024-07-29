import { ref } from 'vue';
import { defineStore } from 'pinia';
import axios from 'axios';

export const useStore = defineStore('store', () => {
  const isClicked = ref('diary');
  const currentMonth = ref(new Date().getMonth() + 1);
  const isFinished = ref(false);
  const colors = ref([]);

  const changeFinishedState = () => {
    isFinished.value = !isFinished.value;
  };

  const changeMonth = (month) => {
    currentMonth.value = month;
  };

  const getColors = async () => {
    const res = await axios.get(`http://34.146.205.159:8000/theme/all/?format=json`);
    colors.value = res.data;
  };

  const clickChangeTheme = async(theme) => {
    const res = await axios.post('http://34.146.205.159:8000/theme/use/?format=json', {
      themeId: theme.themeId,
    });
    await getColors();
  };

  return {
    isClicked,
    currentMonth,
    isFinished,
    changeMonth,
    changeFinishedState,
    getColors,
    clickChangeTheme,
    colors,
  };
});
