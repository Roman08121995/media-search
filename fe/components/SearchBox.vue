<template>
  <div class="search-container">
    <div class="search-box">
      <i class="fas fa-search search-icon"></i>
      <input type="text" v-model="query" placeholder="What are you looking for?" @input="update" />
      <button class="clear-search" @click="clear">
        <i class="fas fa-times"></i>
      </button>
    </div>
    <div class="action-button-container">
      <button class="action-button" @click="submit">
        <span class="button-text">Search and analyze</span>
        <i class="fas fa-arrow-up button-icon"></i>
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
const emit = defineEmits(['search']);
const query = ref('');
function clear() {
  query.value = '';
}
function submit() {
  if (query.value.trim()) emit('search', query.value);
}
function update() {
  // Optional: trigger suggestion updates
}
</script>