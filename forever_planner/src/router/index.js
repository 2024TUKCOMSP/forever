import { createRouter, createWebHistory } from 'vue-router';

import CalendarView from '../views/CalendarView.vue';
import HomeView from '../views/HomeView.vue';

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
  ],
});

export default router;
