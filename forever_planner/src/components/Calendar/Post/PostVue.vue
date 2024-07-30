<template>
  <div class="p-0.5 w-full">
    <div class="justify-end w-full rounded text-2xs flex h-full" :style="backgroundColor">
      <div class="h-full bg-[#ffffffBB]" :class="post.isFinished ? 'w-full rounded' : 'w-[95%] rounded-r'">
        <div class="w-full p-[0.5px] flex items-center justify-center">{{ post.title }}</div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { defineProps, onMounted, ref, computed } from 'vue';
import { storeToRefs } from 'pinia';
import { useStore } from '@/stores/store';

const store = useStore();
const { colors } = storeToRefs(store);
const { getColors } = store;

const usingTheme = ref(null);

const props = defineProps({
  post: {
    type: Object,
    required: true
  },
});

const backgroundColor = computed(() => {
  if (!usingTheme.value) return { backgroundColor: '#ffffff' };
  return { backgroundColor: usingTheme.value.colorList[props.post.category.categoryColor].colorCode };
});

onMounted(async () => {
  await getColors();
  usingTheme.value = colors.value.find(theme => theme.is_use);
});
</script>

<style scoped>
</style>
