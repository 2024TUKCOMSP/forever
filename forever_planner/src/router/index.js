import { createRouter, createWebHistory } from 'vue-router';
import CalendarView from '../views/CalendarView.vue';
import HomeView from '../views/HomeView.vue';
import SettingView from '../views/SettingView.vue';
import ThemeView from '../views/ThemeView.vue';
import RemainingTodoView from '@/views/RemainingTodoView.vue';
import CategoryView from '../views/CategoryView';

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      name: 'calendar',
      component: CalendarView,
    },
    {
      path: '/home',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/setting',
      name: 'setting',
      component : SettingView,
    },
    {
      path: '/theme',
      name: 'theme',
      component: ThemeView,
    }, 
    {
      path: '/remainingTodo',
      name: 'remainingTodo',
      component: RemainingTodoView,
    },
    {
      path: '/category',
      name: 'category',
      component: CategoryView,
    }
  ],
});

export default router;
