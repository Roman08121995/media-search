<template>
  <div v-if="result" class="card">
    <video :src="result.video_url" controls width="300" />
    <p>Confidence: {{ result.confidence }}</p>
    <p>Score: {{ result.score.toFixed(2) }}</p>
    <button @click="analyze">Analyze</button>
  </div>
</template>

<script setup>
const props = defineProps({ result: Object })
const emit = defineEmits(['analyze'])

function analyze() {
  emit('analyze', props.result.video_id)
}
</script>
