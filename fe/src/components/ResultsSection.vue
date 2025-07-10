<template>
  <div class="mt-10">
    <h2 class="text-xl font-bold mb-4">Analysis Results</h2>
    <div class="grid gap-6 md:grid-cols-2 lg:grid-cols-3">
      <div
        v-for="result in results"
        :key="result.video_id"
        class="bg-white shadow-md rounded-lg overflow-hidden"
      >
        <video :src="result.video_url" controls class="w-full" preload="metadata"></video>
        <div class="p-4">
          <p class="text-sm text-gray-600">Score: {{ (result.score * 100).toFixed(2) }}%</p>
          <p class="text-sm text-gray-600">Confidence: {{ result.confidence }}</p>
          <button
            @click="$emit('analyze', result.video_id)"
            class="mt-3 inline-block px-3 py-1 bg-blue-600 text-white text-sm rounded hover:bg-blue-700"
          >
            🔬 Analyze
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
defineProps({ results: Array })
</script>
