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
  const categories = ref([]);
  const currentCategoryId = ref("");
  const selectedCategory = ref([]);
  const editCategory = ref([]);

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
    postDatas.value = [];
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

  const updatePost = async (postId, title, content, categoryId) => {
    const res = await axios.put(`${HOST}calendar/post?format=json`, {
      postId: postId,
      title: title,
      content: content,
      categoryId: categoryId,
      calendarMonth: postMonth.value,
      calendarYear: postYear.value,
      calendarDate: postDate.value,
    });
    getAllCalendar();
  };

  const createPost = async (title, content, categoryId) => {
    const res = await axios.post(`${HOST}calendar/post/create?format=json`, {
      title: title,
      content: content,
      categoryId: categoryId,
      calendarMonth: postMonth.value,
      calendarYear: postYear.value,
      calendarDate: postDate.value,
    });
    getAllCalendar();
  };

  const getCategories = async () => {
    const res = await axios.get(`${HOST}category/all?format=json`);
    categories.value = res.data;
  };

  const createCategory = async (num, title) => {
    const res = await axios.post(`${HOST}category/create`, {
      categoryColor: num,
      categoryTitle: title,
    });
    getCategories();
  };

  const editCurrentCategory = async (id, num, title) => {
    const res = await axios.put(`${HOST}category/edit?format=json`, {
      categoryId: id,
      categoryColor: num,
      categoryTitle: title,
    });
    getCategories();
  };

  const deleteCategory = async (id) => {
    const res = await axios.delete(`${HOST}category/${id}?format=json`, {
      categoryId: id,
    });
    getCategories();
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
    updatePost,
    getCategories,
    categories,
    createPost,
    currentCategoryId,
    selectedCategory,
    createCategory,
    editCategory,
    editCurrentCategory,
    deleteCategory,
  };
});
