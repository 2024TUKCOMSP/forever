<template>
  <div
    class="flex flex-col h-full justify-between text-2xs"
    @touchstart="handleTouchStart"
    @touchend="handleTouchEnd"
  >
    <div v-for="(week, weekIndex) in calendar" :key="weekIndex" class="flex w-full h-full">
      <div
        v-for="(date, dayIndex) in week"
        :key="dayIndex"
        class="w-full h-full flex flex-col items-center justify-start"
        @click="handleClickDateModal(date)"
      >
        <div class="pb-0.5"
          :class="getDateClass(date)"
        >
          {{ date !== '' ? date : '' }}
        </div>
        <PostVue v-if="date !== ''" />
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, watch } from 'vue';
import { startOfMonth, endOfMonth, startOfWeek, endOfWeek, eachDayOfInterval, addMonths, isSameDay } from 'date-fns';
import PostVue from './Post/PostVue.vue';
import { useModalStore } from '@/stores/modalStore.js';
import { useStore } from '@/stores/store.js';

const { handleClickDateModal } = useModalStore();
const { changeMonth } = useStore();

const currentDate = ref(new Date());
const today = new Date();

const touchStartX = ref(0);
const touchEndX = ref(0);

const getCalendar = (date) => {
  const startMonth = startOfMonth(date);
  const endMonth = endOfMonth(date);
  const start = startOfWeek(startMonth, { weekStartsOn: 0 });
  const end = endOfWeek(endMonth, { weekStartsOn: 0 });

  const days = eachDayOfInterval({ start, end });

  const calendar = [];
  let week = [];

  days.forEach((day, index) => {
    if (day.getMonth() === date.getMonth()) {
      week.push(day.getDate());
    } else {
      week.push('');
    }

    if ((index + 1) % 7 === 0) {
      calendar.push(week);
      week = [];
    }
  });

  if (week.length > 0) {
    while (week.length < 7) {
      week.push('');
    }
    calendar.push(week);
  }

  return calendar;
};

const calendar = computed(() => getCalendar(currentDate.value));

const isToday = (date) => {
  if (date === '') return false;
  const day = new Date(currentDate.value.getFullYear(), currentDate.value.getMonth(), date);
  return isSameDay(day, today);
};

const getDateClass = (date) => {
  let className = '';

  if (date === '') return className;

  const dayOfWeek = new Date(currentDate.value.getFullYear(), currentDate.value.getMonth(), date).getDay();
  if (dayOfWeek === 0) { 
    className += ' text-red-500';
  } else if (dayOfWeek === 6) {
    className += ' text-blue-500';
  }

  if (isToday(date)) {
    className = 'text-white';
  }

  return {
    'bg-blue-500 text-white font-bold rounded-full aspect-square flex items-center justify-center': isToday(date),
    [className]: true
  };
};

const changeCurrentMonth = (direction) => {
  currentDate.value = addMonths(currentDate.value, direction);
};

const handleTouchStart = (event) => {
  touchStartX.value = event.touches[0].clientX;
};

const handleTouchEnd = (event) => {
  touchEndX.value = event.changedTouches[0].clientX;
  const diffX = touchStartX.value - touchEndX.value;

  if (Math.abs(diffX) > 50) {
    changeCurrentMonth(diffX > 0 ? 1 : -1);
  }
};

watch(
  () => currentDate.value,
  (newDate) => {
    const month = newDate.getMonth() + 1;
    changeMonth(month);
  },
  { immediate: true }
);
</script>

<style scoped>
</style>
