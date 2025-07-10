<template>
  <div class="flex items-center gap-3 mt-6">
    <input
      v-model="query"
      placeholder="What are you looking for?"
      @keyup.enter="onSearch"
      class="flex-1 px-4 py-2 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-400"
    />
    <button
      @click="onSearch"
      class="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition"
    >
      <i class="fas fa-search"></i> Search
    </button>
  </div>
</template>

<script setup>
import { ref } from 'vue'
const query = ref('')
const emit = defineEmits(['search'])

function onSearch() {
  if (query.value.trim()) emit('search', query.value)
}
</script>