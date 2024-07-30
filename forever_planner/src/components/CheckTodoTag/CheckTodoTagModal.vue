<template>
<div class="checkTodoTagModal" tabindex="-1" v-if="isModalVisible" ref="checkTodoTagModal" @blur="closeModal">
    <button type="button" class="checkTodoTagBtn" value="일상" @click="checkTodoTagClick('일상')">
      <span class="tag1Round">●</span>
      태그명1
    </button><br />
    <button type="button" class="checkTodoTagBtn" value="중요" @click="checkTodoTagClick('중요')">
      <span class="tag2Round">●</span>
      태그명2
    </button><br />
    <button type="button" class="checkTodoTagBtn" value="공부" @click="checkTodoTagClick('공부')">
      <span class="tag3Round">●</span>
      태그명3
    </button><br />
  </div>
</template>
<script>
</script>
<style>
</style>
