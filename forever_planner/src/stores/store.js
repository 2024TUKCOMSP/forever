import { ref } from 'vue';
import { defineStore } from 'pinia';
import axios from 'axios';

export const useStore = defineStore('store', () => {
  const HOST = "http://34.146.205.159:8000/";
  const isClicked = ref('diary');
  const currentMonth = ref(new Date().getMonth() + 1);
  const currentYear = ref(new Date().getFullYear);
  const postMonth = ref(0);
  const postYear = ref(0);
  const colors = ref([]);
  const postDatas = ref([]);
  const currentColors = ref([]);
  const usingTheme = ref([]);
  const postDate = ref(0);

  const changeFinishedState = async (state, postId) => {
    const res = await axios.put(`${HOST}calendar/post/finish?format=json`, {
      postId: postId,
      isFinished: !state,
    });
    getAllCalendar();
  };

  const getColors = async () => {
    const res = await axios.get(`${HOST}theme/all/?format=json`);
    colors.value = res.data;
    usingTheme.value = colors.value.find(theme => theme.is_use);
  };

  const clickChangeTheme = async (theme) => {
    const res = await axios.post(`${HOST}theme/use/?format=json`, {
      themeId: theme.themeId,
    });
    await getColors();
  };

  const getAllCalendar = async () => {
    const res = await axios.post(`${HOST}calendar/all?format=json`, {
      calendarMonth: currentMonth.value,
      calendarYear: currentYear.value,
    });
    postDatas.value = res.data;
  };

  const getCurrentThemeColor = async (themeId) => {
    if(themeId) {
      const res = await axios.get(`${HOST}theme/${themeId}?format=json`);
      currentColors.value = res.data;
    }
  };

  return {
    isClicked,
    changeFinishedState,
    getColors,
    clickChangeTheme,
    colors,
    currentYear,
    currentMonth,
    getAllCalendar,
    postDatas,
    getCurrentThemeColor,
    currentColors,
    usingTheme,
    postMonth,
    postYear,
    postDate,
  };
});
