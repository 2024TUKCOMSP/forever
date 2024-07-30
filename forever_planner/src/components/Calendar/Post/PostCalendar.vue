<template>
  <div class="w-full" :style="getBackgroundColor()">
    <div class="relative w-full bg-[#FFFFFFBB] gap-1.5 flex flex-col py-4" @touchstart="handleTouchStart" @touchend="handleTouchEnd">
      <div class="absolute inset-0 bg-[#00000008]"></div>
      <div class="w-full flex justify-center pb-2">
        <div class="text-lg font-semibold">{{ month }}월 {{ year }}</div>
      </div>
      <div class="flex">
        <div v-for="week in weeks" :key="week" class="w-[14.2%] text-center text-sm">{{ week }}</div>
      </div>
      <div v-for="week in calendar" :key="week[0]?.date" class="flex justify-evenly text-xl">
        <div v-for="day in week" :key="day?.date" class="w-[14.2%] flex z-10 justify-center">
          <div @click="clickGetDate(day)" v-if="day && day.isCurrentMonth" :class="{ 'rounded-full bg-black text-white h-full aspect-square text-center font-semibold': isHighlighted(day) }">
            {{ day.date.getDate() }}
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useModalStore } from '@/stores/modalStore';
import { storeToRefs } from 'pinia';
import { useStore } from '@/stores/store';
import { ref, computed } from 'vue';

const { currentMonth, currentYear, postMonth, postYear, postDate } = storeToRefs(useStore());
const { categoryColor, modalDate } = storeToRefs(useModalStore());
const weeks = ["일", "월", "화", "수", "목", "금", "토"];
const month = ref(currentMonth.value);
const year = ref(currentYear.value);
const date = ref(modalDate.value);
const highlightedMonth = ref(currentMonth.value);
const highlightedYear = ref(currentYear.value);

const getBackgroundColor = () => {
  return { backgroundColor: categoryColor.value };
};

const daysInMonth = (month, year) => {
  return new Date(year, month + 1, 0).getDate();
};

const getFirstDayOfMonth = (month, year) => {
  return new Date(year, month, 1).getDay();
};

const generateCalendar = () => {
  const firstDay = getFirstDayOfMonth(month.value - 1, year.value);
  const totalDays = daysInMonth(month.value - 1, year.value);
  
  let calendar = [];
  let week = [];

  for (let i = 0; i < firstDay; i++) {
    week.push(null);
  }

  for (let day = 1; day <= totalDays; day++) {
    if (week.length === 7) {
      calendar.push(week);
      week = [];
    }
    week.push({ date: new Date(year.value, month.value - 1, day), isCurrentMonth: true });
  }

  if (week.length > 0) {
    while (week.length < 7) {
      week.push(null);
    }
    calendar.push(week);
  }

  return calendar;
};

const calendar = computed(() => generateCalendar());

const isHighlighted = (day) => {
  return day.date.getDate() == date.value && day.date.getMonth() == highlightedMonth.value - 1 && day.date.getFullYear() == highlightedYear.value;
};

const touchStartX = ref(0);
const touchEndX = ref(0);

const handleTouchStart = (event) => {
  touchStartX.value = event.changedTouches[0].screenX;
};

const handleTouchEnd = (event) => {
  touchEndX.value = event.changedTouches[0].screenX;
  handleSwipe();
};

const handleSwipe = () => {
  if (touchEndX.value < touchStartX.value) {
    nextMonth();
  }
  if (touchEndX.value > touchStartX.value) {
    previousMonth();
  }
};

const nextMonth = () => {
  if (month.value === 12) {
    month.value = 1;
    year.value++;
  } else {
    month.value++;
  }
};

const previousMonth = () => {
  if (month.value === 1) {
    month.value = 12;
    year.value--;
  } else {
    month.value--;
  }
};

const clickGetDate = (day) => {
  date.value = day.date.getDate();
  highlightedMonth.value = month.value;
  highlightedYear.value = year.value;
  postDate.value = date.value;
  postMonth.value = month.value;
  postYear.value = year.value;
};
</script>

<style scoped>
</style>
