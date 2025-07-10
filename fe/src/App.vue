<template>
  <div class="min-h-screen bg-gray-100">
    <Navbar />
    <main class="px-4 max-w-7xl mx-auto py-6">
      <SearchBox @search="handleSearch" />
      <SampleVideos v-if="!loading && !results.length && !searching" />
      <LoadingSpinner v-if="loading" />
      <ResultsSection v-if="results.length" :results="results" @analyze="openAnalysis" />
      <AnalysisModal v-if="showModal" :video-id="selectedVideoId" @close="closeModal" />
    </main>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import Navbar from './components/Navbar.vue'
import SearchBox from './components/SearchBox.vue'
import SampleVideos from './components/SampleVideos.vue'
import LoadingSpinner from './components/LoadingSpinner.vue'
import ResultsSection from './components/ResultsSection.vue'
import AnalysisModal from './components/AnalysisModal.vue'

const results = ref([])
const loading = ref(false)
const searching = ref(false)
const showModal = ref(false)
const selectedVideoId = ref(null)

async function handleSearch(query) {
  loading.value = true
  results.value = []
  searching.value = true
  try {
    const res = await fetch('/search', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ query })
    })
    results.value = await res.json()
  } catch (err) {
    console.error(err)
  } finally {
    loading.value = false
  }
}

function openAnalysis(videoId) {
  selectedVideoId.value = videoId
  showModal.value = true
}

function closeModal() {
  showModal.value = false
  selectedVideoId.value = null
}
</script>

<style>
body {
  font-family: 'Segoe UI', sans-serif;
}
</style>