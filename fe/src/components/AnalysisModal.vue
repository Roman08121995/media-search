<template>
  <div class="fixed inset-0 bg-black bg-opacity-50 flex justify-center items-center z-50">
    <div class="bg-white max-w-2xl w-full p-6 rounded-xl shadow-lg relative">
      <button @click="$emit('close')" class="absolute top-3 right-3 text-xl">&times;</button>
      <h2 class="text-xl font-semibold mb-4">AI Analysis</h2>
      <div v-if="loading">
        <LoadingSpinner />
      </div>
      <div v-else>
        <video :src="videoUrl" controls class="w-full rounded-lg" v-if="videoUrl" />
        <p class="mt-4 whitespace-pre-line">{{ analysis }}</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import LoadingSpinner from './LoadingSpinner.vue'

const props = defineProps({ videoId: String })
const emit = defineEmits(['close'])
const analysis = ref('')
const videoUrl = ref('')
const loading = ref(true)

onMounted(async () => {
  try {
    const res = await fetch(`/analyze/${props.videoId}`)
    const data = await res.json()
    analysis.value = data.analysis
    videoUrl.value = data.video_url
  } catch (err) {
    analysis.value = 'Failed to load analysis.'
  } finally {
    loading.value = false
  }
})
</script>
