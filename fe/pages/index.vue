<template>
  <div>
    <Hero />
    <SearchBox @search="onSearch" />
    <SampleVideos v-if="!hasSearched" />
    <LoadingSpinner v-if="isLoading" />
    <ResultsGrid v-if="results.length" :results="results" @analyze="onAnalyze" />
    <ErrorState v-if="error" :message="error" @retry="onSearch" />
    <AnalysisModal v-if="showModal" :videoId="selectedVideoId" @close="() => (showModal = false)" />
  </div>
</template>

<script setup>
import { ref } from 'vue';
import Hero from '@/components/Hero.vue';
import SearchBox from '@/components/SearchBox.vue';
import SampleVideos from '@/components/SampleVideos.vue';
import LoadingSpinner from '@/components/LoadingSpinner.vue';
import ResultsGrid from '@/components/ResultsGrid.vue';
import ErrorState from '@/components/ErrorState.vue';
import AnalysisModal from '@/components/AnalysisModal.vue';

const isLoading = ref(false);
const error = ref('');
const results = ref([]);
const showModal = ref(false);
const selectedVideoId = ref(null);
const hasSearched = ref(false);

async function onSearch(query) {
  isLoading.value = true;
  error.value = '';
  hasSearched.value = true;
  try {
    const res = await $fetch('/api/search', {
      method: 'POST',
      body: { query }
    });
    results.value = res;
  } catch (e) {
    error.value = 'Search failed. Try again.';
  } finally {
    isLoading.value = false;
  }
}

function onAnalyze(videoId) {
  selectedVideoId.value = videoId;
  showModal.value = true;
}
</script>